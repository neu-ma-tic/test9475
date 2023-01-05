import { IExecute } from "../../interfaces/IEvents";

export const name:string = 'ready';
export const execute:IExecute = async (client) => {
  console.log("I am online");
}

// module.exports = () => {
//   console.log("I am online");
// };
