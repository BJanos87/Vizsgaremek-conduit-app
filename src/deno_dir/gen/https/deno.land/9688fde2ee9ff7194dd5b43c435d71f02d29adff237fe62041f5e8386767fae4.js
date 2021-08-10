import * as bcrypt from "./bcrypt/bcrypt.ts";
export async function hash(plaintext, salt = undefined) {
    let worker = new Worker(new URL("worker.ts", import.meta.url).toString(), { type: "module", deno: true });
    worker.postMessage({
        action: "hash",
        payload: {
            plaintext,
            salt,
        },
    });
    return new Promise((resolve) => {
        worker.onmessage = (event) => {
            resolve(event.data);
            worker.terminate();
        };
    });
}
export async function genSalt(log_rounds = undefined) {
    let worker = new Worker(new URL("worker.ts", import.meta.url).toString(), { type: "module", deno: true });
    worker.postMessage({
        action: "genSalt",
        payload: {
            log_rounds,
        },
    });
    return new Promise((resolve) => {
        worker.onmessage = (event) => {
            resolve(event.data);
            worker.terminate();
        };
    });
}
export async function compare(plaintext, hash) {
    let worker = new Worker(new URL("worker.ts", import.meta.url).toString(), { type: "module", deno: true });
    worker.postMessage({
        action: "compare",
        payload: {
            plaintext,
            hash,
        },
    });
    return new Promise((resolve) => {
        worker.onmessage = (event) => {
            resolve(event.data);
            worker.terminate();
        };
    });
}
export function compareSync(plaintext, hash) {
    try {
        return bcrypt.checkpw(plaintext, hash);
    }
    catch {
        return false;
    }
}
export function genSaltSync(log_rounds = undefined) {
    return bcrypt.gensalt(log_rounds);
}
export function hashSync(plaintext, salt = undefined) {
    return bcrypt.hashpw(plaintext, salt);
}
//# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoibWFpbi5qcyIsInNvdXJjZVJvb3QiOiIiLCJzb3VyY2VzIjpbIm1haW4udHMiXSwibmFtZXMiOltdLCJtYXBwaW5ncyI6IkFBQUEsT0FBTyxLQUFLLE1BQU0sTUFBTSxvQkFBb0IsQ0FBQztBQVc3QyxNQUFNLENBQUMsS0FBSyxVQUFVLElBQUksQ0FDeEIsU0FBaUIsRUFDakIsT0FBMkIsU0FBUztJQUVwQyxJQUFJLE1BQU0sR0FBRyxJQUFJLE1BQU0sQ0FDckIsSUFBSSxHQUFHLENBQUMsV0FBVyxFQUFFLE1BQU0sQ0FBQyxJQUFJLENBQUMsR0FBRyxDQUFDLENBQUMsUUFBUSxFQUFFLEVBQ2hELEVBQUUsSUFBSSxFQUFFLFFBQVEsRUFBRSxJQUFJLEVBQUUsSUFBSSxFQUFFLENBQy9CLENBQUM7SUFFRixNQUFNLENBQUMsV0FBVyxDQUFDO1FBQ2pCLE1BQU0sRUFBRSxNQUFNO1FBQ2QsT0FBTyxFQUFFO1lBQ1AsU0FBUztZQUNULElBQUk7U0FDTDtLQUNGLENBQUMsQ0FBQztJQUVILE9BQU8sSUFBSSxPQUFPLENBQUMsQ0FBQyxPQUFPLEVBQUUsRUFBRTtRQUM3QixNQUFNLENBQUMsU0FBUyxHQUFHLENBQUMsS0FBSyxFQUFFLEVBQUU7WUFDM0IsT0FBTyxDQUFDLEtBQUssQ0FBQyxJQUFJLENBQUMsQ0FBQztZQUNwQixNQUFNLENBQUMsU0FBUyxFQUFFLENBQUM7UUFDckIsQ0FBQyxDQUFDO0lBQ0osQ0FBQyxDQUFDLENBQUM7QUFDTCxDQUFDO0FBVUQsTUFBTSxDQUFDLEtBQUssVUFBVSxPQUFPLENBQzNCLGFBQWlDLFNBQVM7SUFFMUMsSUFBSSxNQUFNLEdBQUcsSUFBSSxNQUFNLENBQ3JCLElBQUksR0FBRyxDQUFDLFdBQVcsRUFBRSxNQUFNLENBQUMsSUFBSSxDQUFDLEdBQUcsQ0FBQyxDQUFDLFFBQVEsRUFBRSxFQUNoRCxFQUFFLElBQUksRUFBRSxRQUFRLEVBQUUsSUFBSSxFQUFFLElBQUksRUFBRSxDQUMvQixDQUFDO0lBRUYsTUFBTSxDQUFDLFdBQVcsQ0FBQztRQUNqQixNQUFNLEVBQUUsU0FBUztRQUNqQixPQUFPLEVBQUU7WUFDUCxVQUFVO1NBQ1g7S0FDRixDQUFDLENBQUM7SUFFSCxPQUFPLElBQUksT0FBTyxDQUFDLENBQUMsT0FBTyxFQUFFLEVBQUU7UUFDN0IsTUFBTSxDQUFDLFNBQVMsR0FBRyxDQUFDLEtBQUssRUFBRSxFQUFFO1lBQzNCLE9BQU8sQ0FBQyxLQUFLLENBQUMsSUFBSSxDQUFDLENBQUM7WUFDcEIsTUFBTSxDQUFDLFNBQVMsRUFBRSxDQUFDO1FBQ3JCLENBQUMsQ0FBQztJQUNKLENBQUMsQ0FBQyxDQUFDO0FBQ0wsQ0FBQztBQVdELE1BQU0sQ0FBQyxLQUFLLFVBQVUsT0FBTyxDQUMzQixTQUFpQixFQUNqQixJQUFZO0lBRVosSUFBSSxNQUFNLEdBQUcsSUFBSSxNQUFNLENBQ3JCLElBQUksR0FBRyxDQUFDLFdBQVcsRUFBRSxNQUFNLENBQUMsSUFBSSxDQUFDLEdBQUcsQ0FBQyxDQUFDLFFBQVEsRUFBRSxFQUNoRCxFQUFFLElBQUksRUFBRSxRQUFRLEVBQUUsSUFBSSxFQUFFLElBQUksRUFBRSxDQUMvQixDQUFDO0lBRUYsTUFBTSxDQUFDLFdBQVcsQ0FBQztRQUNqQixNQUFNLEVBQUUsU0FBUztRQUNqQixPQUFPLEVBQUU7WUFDUCxTQUFTO1lBQ1QsSUFBSTtTQUNMO0tBQ0YsQ0FBQyxDQUFDO0lBRUgsT0FBTyxJQUFJLE9BQU8sQ0FBQyxDQUFDLE9BQU8sRUFBRSxFQUFFO1FBQzdCLE1BQU0sQ0FBQyxTQUFTLEdBQUcsQ0FBQyxLQUFLLEVBQUUsRUFBRTtZQUMzQixPQUFPLENBQUMsS0FBSyxDQUFDLElBQUksQ0FBQyxDQUFDO1lBQ3BCLE1BQU0sQ0FBQyxTQUFTLEVBQUUsQ0FBQztRQUNyQixDQUFDLENBQUM7SUFDSixDQUFDLENBQUMsQ0FBQztBQUNMLENBQUM7QUFZRCxNQUFNLFVBQVUsV0FBVyxDQUFDLFNBQWlCLEVBQUUsSUFBWTtJQUN6RCxJQUFJO1FBQ0YsT0FBTyxNQUFNLENBQUMsT0FBTyxDQUFDLFNBQVMsRUFBRSxJQUFJLENBQUMsQ0FBQztLQUN4QztJQUFDLE1BQU07UUFDTixPQUFPLEtBQUssQ0FBQztLQUNkO0FBQ0gsQ0FBQztBQVdELE1BQU0sVUFBVSxXQUFXLENBQ3pCLGFBQWlDLFNBQVM7SUFFMUMsT0FBTyxNQUFNLENBQUMsT0FBTyxDQUFDLFVBQVUsQ0FBQyxDQUFDO0FBQ3BDLENBQUM7QUFZRCxNQUFNLFVBQVUsUUFBUSxDQUN0QixTQUFpQixFQUNqQixPQUEyQixTQUFTO0lBRXBDLE9BQU8sTUFBTSxDQUFDLE1BQU0sQ0FBQyxTQUFTLEVBQUUsSUFBSSxDQUFDLENBQUM7QUFDeEMsQ0FBQyJ9