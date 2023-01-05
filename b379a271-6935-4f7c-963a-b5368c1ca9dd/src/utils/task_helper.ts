import { bgYellow, black, Collection } from "../../deps.ts";
import { Task } from "./../types/tasks.ts";
import { bot } from "../../cache.ts";
import { log } from "./logger.ts";

export function registerTasks() {
  for (const task of bot.tasks.values()) {
    bot.runningTasks.initialTimeouts.push(
      setTimeout(async () => {
        log.info(`[TASK: ${bgYellow(black(task.name))}] Started.`);
        try {
          await task.execute();
        } catch (error) {
          log.error(error);
        }

        bot.runningTasks.initialTimeouts.push(
          setInterval(async () => {
            if (!bot.fullyReady) return;
            log.info(`[TASK: ${bgYellow(black(task.name))}] Started.`);
            try {
              await task.execute();
            } catch (error) {
              log.error(error);
            }
          }, task.interval),
        );
      }, task.interval - (Date.now() % task.interval)),
    );
  }
}

export function clearTasks() {
  for (const timeout of bot.runningTasks.initialTimeouts) clearTimeout(timeout);
  for (const task of bot.runningTasks.intervals) clearInterval(task);

  bot.tasks = new Collection<string, Task>();
  bot.runningTasks = { initialTimeouts: [], intervals: [] };
}
