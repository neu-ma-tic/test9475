import { Bot } from "../Bot";

export interface IExecute {(client: Bot, ...params)};

export interface IEvent{
    name:string,
    execute: IExecute    
}