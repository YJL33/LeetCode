/*
Shortest Job First
processor dealing with jobs,
for multiple jobs in queue, it will process the one has the shortest runtime.
if multiple jobs having the same runtime, it will process the one arrive first.
return the avg wait time.
*/
import java.util.*;
public class Solution {
    static class Process
    {
        int arrTime;
        int exeTime;
        public Process(int arrTime, int exeTime)
        {
            this.arrTime = arrTime;
            this.exeTime = exeTime;
        }
    }
    public static double SJL(int[] arriveTime, int[] runTime)
    {
        if (arriveTime == null || arriveTime.length == 0) return 0;
        PriorityQueue<Process> pq = new PriorityQueue<>(new Comparator<Process>(){
            @Override
            public int compare(Process p1, Process p2) {
                if (p1.exeTime == p2.exeTime) return p1.arrTime - p2.arrTime;
                else return p1.exeTime - p2.exeTime;
            }
        });
        int wait = 0, t = 0, i = 0;
        while (i < arriveTime.length || !pq.isEmpty())
        {
            // if pq is empty => add one
            if (pq.isEmpty())
            {
                pq.add(new Process(arriveTime[i], runTime[i]));
                i++;
            }
            // if not => poll one from priority queue.
            else
            {
                Process cur = pq.poll();
                if (t > cur.arrTime) wait += t-cur.arrTime;     // check whether it's be waited
                else t = cur.arrTime;
                t += cur.exeTime;                               // update time
                while (i < arriveTime.length && arriveTime[i] <= t) {       // add new tasks
                    pq.add(new Process(arriveTime[i], runTime[i]));
                    i++;
                }
            }
        }
        return (wait + 0.0)/arriveTime.length;
    }

    public static double SJL2(int[] req, int[] dur)
    {
        if(req == null || req.length == 0) return 0;
        PriorityQueue<Process> queue = new PriorityQueue<>(new Comparator<Process>()
        {
            @Override
            public int compare(Process a, Process b)
            {
                if(a.exeTime == b.exeTime) return a.arrTime - b.arrTime;
                else return a.exeTime - b.exeTime;
            }
        });
        int t = 0, sum = 0, i = 0;
        while(i < req.length || !queue.isEmpty())
        {
            if(queue.isEmpty())
            {
                queue.offer(new Process(req[i], dur[i]));
                t = req[i];
                i++;
            }
            else
            {
                Process p = queue.poll();
                sum += (t - p.arrTime);
                t += p.exeTime;
                while(i < req.length && req[i] <= t)
                {
                    queue.offer(new Process(req[i], dur[i]));
                    i++;
                }
            }
        }
        return (sum + 0.0) / req.length;
    }

    public static void main(String[] args)
    {
        int[] req = {1, 3, 3, 6, 6, 6, 7};
        int[] dur = {2 ,2 ,3 ,2, 4, 4, 2};
        System.out.println(SJL(req, dur));
        System.out.println(SJL2(req, dur));
    }
}