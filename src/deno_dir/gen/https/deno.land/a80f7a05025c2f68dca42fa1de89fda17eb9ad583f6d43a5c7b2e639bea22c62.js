import { Buffer } from "./buffer.ts";
export async function readAll(r) {
    const buf = new Buffer();
    await buf.readFrom(r);
    return buf.bytes();
}
export function readAllSync(r) {
    const buf = new Buffer();
    buf.readFromSync(r);
    return buf.bytes();
}
export async function writeAll(w, arr) {
    let nwritten = 0;
    while (nwritten < arr.length) {
        nwritten += await w.write(arr.subarray(nwritten));
    }
}
export function writeAllSync(w, arr) {
    let nwritten = 0;
    while (nwritten < arr.length) {
        nwritten += w.writeSync(arr.subarray(nwritten));
    }
}
//# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoidXRpbC5qcyIsInNvdXJjZVJvb3QiOiIiLCJzb3VyY2VzIjpbInV0aWwudHMiXSwibmFtZXMiOltdLCJtYXBwaW5ncyI6IkFBQUEsT0FBTyxFQUFFLE1BQU0sRUFBRSxNQUFNLGFBQWEsQ0FBQztBQXNCckMsTUFBTSxDQUFDLEtBQUssVUFBVSxPQUFPLENBQUMsQ0FBYztJQUMxQyxNQUFNLEdBQUcsR0FBRyxJQUFJLE1BQU0sRUFBRSxDQUFDO0lBQ3pCLE1BQU0sR0FBRyxDQUFDLFFBQVEsQ0FBQyxDQUFDLENBQUMsQ0FBQztJQUN0QixPQUFPLEdBQUcsQ0FBQyxLQUFLLEVBQUUsQ0FBQztBQUNyQixDQUFDO0FBcUJELE1BQU0sVUFBVSxXQUFXLENBQUMsQ0FBa0I7SUFDNUMsTUFBTSxHQUFHLEdBQUcsSUFBSSxNQUFNLEVBQUUsQ0FBQztJQUN6QixHQUFHLENBQUMsWUFBWSxDQUFDLENBQUMsQ0FBQyxDQUFDO0lBQ3BCLE9BQU8sR0FBRyxDQUFDLEtBQUssRUFBRSxDQUFDO0FBQ3JCLENBQUM7QUFzQkQsTUFBTSxDQUFDLEtBQUssVUFBVSxRQUFRLENBQUMsQ0FBYyxFQUFFLEdBQWU7SUFDNUQsSUFBSSxRQUFRLEdBQUcsQ0FBQyxDQUFDO0lBQ2pCLE9BQU8sUUFBUSxHQUFHLEdBQUcsQ0FBQyxNQUFNLEVBQUU7UUFDNUIsUUFBUSxJQUFJLE1BQU0sQ0FBQyxDQUFDLEtBQUssQ0FBQyxHQUFHLENBQUMsUUFBUSxDQUFDLFFBQVEsQ0FBQyxDQUFDLENBQUM7S0FDbkQ7QUFDSCxDQUFDO0FBdUJELE1BQU0sVUFBVSxZQUFZLENBQUMsQ0FBa0IsRUFBRSxHQUFlO0lBQzlELElBQUksUUFBUSxHQUFHLENBQUMsQ0FBQztJQUNqQixPQUFPLFFBQVEsR0FBRyxHQUFHLENBQUMsTUFBTSxFQUFFO1FBQzVCLFFBQVEsSUFBSSxDQUFDLENBQUMsU0FBUyxDQUFDLEdBQUcsQ0FBQyxRQUFRLENBQUMsUUFBUSxDQUFDLENBQUMsQ0FBQztLQUNqRDtBQUNILENBQUMifQ==