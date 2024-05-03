using System;
using System.Collections.Generic;

class Lockboxes
{
    public static bool CanUnlockAll(List<List<int>> boxes)
    {
        int n = boxes.Count;
        HashSet<int> seenBoxes = new HashSet<int>();
        HashSet<int> unseenBoxes = new HashSet<int>(boxes[0]);
        seenBoxes.Add(0);
        while (unseenBoxes.Count > 0)
        {
            int boxIdx = unseenBoxes.Pop();
            if (boxIdx < 0 || boxIdx >= n)
                continue;
            if (!seenBoxes.Contains(boxIdx))
            {
                foreach (int key in boxes[boxIdx])
                {
                    unseenBoxes.Add(key);
                }
                seenBoxes.Add(boxIdx);
            }
        }
        return n == seenBoxes.Count;
    }
}
