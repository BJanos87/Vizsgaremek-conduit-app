import { parseArray } from "./array_parser.ts";
const BACKSLASH_BYTE_VALUE = 92;
const BC_RE = /BC$/;
const DATE_RE = /^(\d{1,})-(\d{2})-(\d{2})$/;
const DATETIME_RE = /^(\d{1,})-(\d{2})-(\d{2}) (\d{2}):(\d{2}):(\d{2})(\.\d{1,})?/;
const HEX = 16;
const HEX_PREFIX_REGEX = /^\\x/;
const TIMEZONE_RE = /([Z+-])(\d{2})?:?(\d{2})?:?(\d{2})?/;
export function decodeBigint(value) {
    return BigInt(value);
}
export function decodeBigintArray(value) {
    return parseArray(value, (x) => BigInt(x));
}
export function decodeBoolean(value) {
    return value[0] === "t";
}
export function decodeBooleanArray(value) {
    return parseArray(value, (x) => x[0] === "t");
}
export function decodeBox(value) {
    const [a, b] = value.match(/\(.*?\)/g) || [];
    return {
        a: decodePoint(a),
        b: decodePoint(b),
    };
}
export function decodeBoxArray(value) {
    return parseArray(value, decodeBox);
}
export function decodeBytea(byteaStr) {
    if (HEX_PREFIX_REGEX.test(byteaStr)) {
        return decodeByteaHex(byteaStr);
    }
    else {
        return decodeByteaEscape(byteaStr);
    }
}
export function decodeByteaArray(value) {
    return parseArray(value, decodeBytea);
}
function decodeByteaEscape(byteaStr) {
    const bytes = [];
    let i = 0;
    let k = 0;
    while (i < byteaStr.length) {
        if (byteaStr[i] !== "\\") {
            bytes.push(byteaStr.charCodeAt(i));
            ++i;
        }
        else {
            if (/[0-7]{3}/.test(byteaStr.substr(i + 1, 3))) {
                bytes.push(parseInt(byteaStr.substr(i + 1, 3), 8));
                i += 4;
            }
            else {
                let backslashes = 1;
                while (i + backslashes < byteaStr.length &&
                    byteaStr[i + backslashes] === "\\") {
                    backslashes++;
                }
                for (k = 0; k < Math.floor(backslashes / 2); ++k) {
                    bytes.push(BACKSLASH_BYTE_VALUE);
                }
                i += Math.floor(backslashes / 2) * 2;
            }
        }
    }
    return new Uint8Array(bytes);
}
function decodeByteaHex(byteaStr) {
    const bytesStr = byteaStr.slice(2);
    const bytes = new Uint8Array(bytesStr.length / 2);
    for (let i = 0, j = 0; i < bytesStr.length; i += 2, j++) {
        bytes[j] = parseInt(bytesStr[i] + bytesStr[i + 1], HEX);
    }
    return bytes;
}
export function decodeCircle(value) {
    const [point, radius] = value.substring(1, value.length - 1).split(/,(?![^(]*\))/);
    return {
        point: decodePoint(point),
        radius: radius,
    };
}
export function decodeCircleArray(value) {
    return parseArray(value, decodeCircle);
}
export function decodeDate(dateStr) {
    if (dateStr === "infinity") {
        return Number(Infinity);
    }
    else if (dateStr === "-infinity") {
        return Number(-Infinity);
    }
    const matches = DATE_RE.exec(dateStr);
    if (!matches) {
        throw new Error(`"${dateStr}" could not be parsed to date`);
    }
    const year = parseInt(matches[1], 10);
    const month = parseInt(matches[2], 10) - 1;
    const day = parseInt(matches[3], 10);
    const date = new Date(year, month, day);
    date.setUTCFullYear(year);
    return date;
}
export function decodeDateArray(value) {
    return parseArray(value, decodeDate);
}
export function decodeDatetime(dateStr) {
    const matches = DATETIME_RE.exec(dateStr);
    if (!matches) {
        return decodeDate(dateStr);
    }
    const isBC = BC_RE.test(dateStr);
    const year = parseInt(matches[1], 10) * (isBC ? -1 : 1);
    const month = parseInt(matches[2], 10) - 1;
    const day = parseInt(matches[3], 10);
    const hour = parseInt(matches[4], 10);
    const minute = parseInt(matches[5], 10);
    const second = parseInt(matches[6], 10);
    const msMatch = matches[7];
    const ms = msMatch ? 1000 * parseFloat(msMatch) : 0;
    let date;
    const offset = decodeTimezoneOffset(dateStr);
    if (offset === null) {
        date = new Date(year, month, day, hour, minute, second, ms);
    }
    else {
        const utc = Date.UTC(year, month, day, hour, minute, second, ms);
        date = new Date(utc + offset);
    }
    date.setUTCFullYear(year);
    return date;
}
export function decodeDatetimeArray(value) {
    return parseArray(value, decodeDatetime);
}
export function decodeInt(value) {
    return parseInt(value, 10);
}
export function decodeIntArray(value) {
    if (!value)
        return null;
    return parseArray(value, decodeInt);
}
export function decodeJson(value) {
    return JSON.parse(value);
}
export function decodeJsonArray(value) {
    return parseArray(value, JSON.parse);
}
export function decodeLine(value) {
    const [a, b, c] = value.substring(1, value.length - 1).split(",");
    return {
        a: a,
        b: b,
        c: c,
    };
}
export function decodeLineArray(value) {
    return parseArray(value, decodeLine);
}
export function decodeLineSegment(value) {
    const [a, b] = value
        .substring(1, value.length - 1)
        .match(/\(.*?\)/g) || [];
    return {
        a: decodePoint(a),
        b: decodePoint(b),
    };
}
export function decodeLineSegmentArray(value) {
    return parseArray(value, decodeLineSegment);
}
export function decodePath(value) {
    const points = value.substring(1, value.length - 1).split(/,(?![^(]*\))/);
    return points.map(decodePoint);
}
export function decodePathArray(value) {
    return parseArray(value, decodePath);
}
export function decodePoint(value) {
    const [x, y] = value.substring(1, value.length - 1).split(",");
    if (Number.isNaN(parseFloat(x)) || Number.isNaN(parseFloat(y))) {
        throw new Error(`Invalid point value: "${Number.isNaN(parseFloat(x)) ? x : y}"`);
    }
    return {
        x: x,
        y: y,
    };
}
export function decodePointArray(value) {
    return parseArray(value, decodePoint);
}
export function decodePolygon(value) {
    return decodePath(value);
}
export function decodePolygonArray(value) {
    return parseArray(value, decodePolygon);
}
export function decodeStringArray(value) {
    if (!value)
        return null;
    return parseArray(value);
}
function decodeTimezoneOffset(dateStr) {
    const timeStr = dateStr.split(" ")[1];
    const matches = TIMEZONE_RE.exec(timeStr);
    if (!matches) {
        return null;
    }
    const type = matches[1];
    if (type === "Z") {
        return 0;
    }
    const sign = type === "-" ? 1 : -1;
    const hours = parseInt(matches[2], 10);
    const minutes = parseInt(matches[3] || "0", 10);
    const seconds = parseInt(matches[4] || "0", 10);
    const offset = hours * 3600 + minutes * 60 + seconds;
    return sign * offset * 1000;
}
export function decodeTid(value) {
    const [x, y] = value.substring(1, value.length - 1).split(",");
    return [BigInt(x), BigInt(y)];
}
export function decodeTidArray(value) {
    return parseArray(value, decodeTid);
}
//# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoiZGVjb2RlcnMuanMiLCJzb3VyY2VSb290IjoiIiwic291cmNlcyI6WyJkZWNvZGVycy50cyJdLCJuYW1lcyI6W10sIm1hcHBpbmdzIjoiQUFBQSxPQUFPLEVBQUUsVUFBVSxFQUFFLE1BQU0sbUJBQW1CLENBQUM7QUFnQi9DLE1BQU0sb0JBQW9CLEdBQUcsRUFBRSxDQUFDO0FBQ2hDLE1BQU0sS0FBSyxHQUFHLEtBQUssQ0FBQztBQUNwQixNQUFNLE9BQU8sR0FBRyw0QkFBNEIsQ0FBQztBQUM3QyxNQUFNLFdBQVcsR0FDZiw4REFBOEQsQ0FBQztBQUNqRSxNQUFNLEdBQUcsR0FBRyxFQUFFLENBQUM7QUFDZixNQUFNLGdCQUFnQixHQUFHLE1BQU0sQ0FBQztBQUNoQyxNQUFNLFdBQVcsR0FBRyxxQ0FBcUMsQ0FBQztBQUUxRCxNQUFNLFVBQVUsWUFBWSxDQUFDLEtBQWE7SUFDeEMsT0FBTyxNQUFNLENBQUMsS0FBSyxDQUFDLENBQUM7QUFDdkIsQ0FBQztBQUVELE1BQU0sVUFBVSxpQkFBaUIsQ0FBQyxLQUFhO0lBQzdDLE9BQU8sVUFBVSxDQUFDLEtBQUssRUFBRSxDQUFDLENBQUMsRUFBRSxFQUFFLENBQUMsTUFBTSxDQUFDLENBQUMsQ0FBQyxDQUFDLENBQUM7QUFDN0MsQ0FBQztBQUVELE1BQU0sVUFBVSxhQUFhLENBQUMsS0FBYTtJQUN6QyxPQUFPLEtBQUssQ0FBQyxDQUFDLENBQUMsS0FBSyxHQUFHLENBQUM7QUFDMUIsQ0FBQztBQUVELE1BQU0sVUFBVSxrQkFBa0IsQ0FBQyxLQUFhO0lBQzlDLE9BQU8sVUFBVSxDQUFDLEtBQUssRUFBRSxDQUFDLENBQUMsRUFBRSxFQUFFLENBQUMsQ0FBQyxDQUFDLENBQUMsQ0FBQyxLQUFLLEdBQUcsQ0FBQyxDQUFDO0FBQ2hELENBQUM7QUFFRCxNQUFNLFVBQVUsU0FBUyxDQUFDLEtBQWE7SUFDckMsTUFBTSxDQUFDLENBQUMsRUFBRSxDQUFDLENBQUMsR0FBRyxLQUFLLENBQUMsS0FBSyxDQUFDLFVBQVUsQ0FB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QUMsQ0FBQztJQUNoRCxNQUFNLE9BQU8sR0FBRyxRQUFRLENBQUMsT0FBTyxDQUFDLENBQUMsQ0FBQyxJQUFJLEdBQUcsRUFBRSxFQUFFLENBQUMsQ0FBQztJQUVoRCxNQUFNLE1BQU0sR0FBRyxLQUFLLEdBQUcsSUFBSSxHQUFHLE9BQU8sR0FBRyxFQUFFLEdBQUcsT0FBTyxDQUFDO0lBRXJELE9BQU8sSUFBSSxHQUFHLE1BQU0sR0FBRyxJQUFJLENBQUM7QUFDOUIsQ0FBQztBQUVELE1BQU0sVUFBVSxTQUFTLENBQUMsS0FBYTtJQUNyQyxNQUFNLENBQUMsQ0FBQyxFQUFFLENBQUMsQ0FBQyxHQUFHLEtBQUssQ0FBQyxTQUFTLENBQUMsQ0FBQyxFQUFFLEtBQUssQ0FBQyxNQUFNLEdBQUcsQ0FBQyxDQUFDLENBQUMsS0FBSyxDQUFDLEdBQUcsQ0FBQyxDQUFDO0lBRS9ELE9BQU8sQ0FBQyxNQUFNLENBQUMsQ0FBQyxDQUFDLEVBQUUsTUFBTSxDQUFDLENBQUMsQ0FBQyxDQUFDLENBQUM7QUFDaEMsQ0FBQztBQUVELE1BQU0sVUFBVSxjQUFjLENBQUMsS0FBYTtJQUMxQyxPQUFPLFVBQVUsQ0FBQyxLQUFLLEVBQUUsU0FBUyxDQUFDLENBQUM7QUFDdEMsQ0FBQyJ9