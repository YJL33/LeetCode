/*
Round Robin
*/
import java.util.*;
 
public class Solution {
    static class Task
    {
        int arrive;
        int remain;
        public Task(int arrive, int remain)
        {
            this.arrive = arrive;
            this.remain = remain;
        }
    }
    public static double roundRobin(int[] arriveTime, int[] runTime, int slot)
    {
        Queue<Task> queue = new LinkedList<>();
        int t = 0, wait = 0, i = 0;

        while (!queue.isEmpty() || i < arriveTime.length) {
            if (queue.isEmpty())
            {
                queue.add(new Task(arriveTime[i], runTime[i]));
                i++;
            }
            else
            {
                Task current = queue.poll();
                // System.out.print("t = ");
                // System.out.print(t);
                // System.out.print("  ");
                // System.out.print(current.arrive);
                // System.out.print(" , ");
                // System.out.print(current.remain);
                // System.out.print("\n");
                if (t > current.arrive) wait += (t-current.arrive);
                else t = current.arrive;
                if (current.remain <= slot) {
                    t += current.remain;
                }
                else
                {
                    t += slot;
                    current.remain -= slot;
                    current.arrive = t;
                    while (i < arriveTime.length && arriveTime[i] <= t) {
                        queue.add(new Task(arriveTime[i], runTime[i]));
                        i++;
                    }
                    queue.add(current);
                }
                // System.out.print("now wait: ");
                // System.out.print(wait);
                // System.out.print("\n");
            }
        }

        return (wait + 0.0)/arriveTime.length;
    }

    public static double roundRobin2(int[] arriveTime, int[] runTime, int slot)
    {
        Queue<Task> queue = new LinkedList<>();
        int i = 0, t = 0, wait = 0;
        while(i < arriveTime.length || !queue.isEmpty())
        {
            if(!queue.isEmpty())
            {
                Task peek = queue.poll();
                wait += (t - peek.arrive);
                if(peek.remain > slot) 
                {
                    t += slot;
                    peek.remain -= slot;
                    peek.arrive = t;
                }
                else
                {
                    t += peek.remain;
                    peek.remain = 0;
                    peek.arrive = t;
                }
                while(i < arriveTime.length && arriveTime[i] <= t)
                {
                    queue.offer(new Task(arriveTime[i], runTime[i]));
                    i++;
                }
                 
                if(peek.remain != 0) queue.offer(peek);
            }
            else
            {
                queue.offer(new Task(arriveTime[i], runTime[i]));
                t = arriveTime[i];
                i++;
            }
        }
        return (wait + 0.0) / arriveTime.length;
    }

    public static void main(String[] args) {
        // TODO Auto-generated method stub
        int[] arriveTime = {0, 1, 3, 9};
        int[] runTime = {2, 1, 7, 5};
        System.out.println(roundRobin(arriveTime, runTime, 2));
        System.out.println(roundRobin2(arriveTime, runTime, 2));

    }
}