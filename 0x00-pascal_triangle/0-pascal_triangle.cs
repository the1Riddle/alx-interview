/** c-sharp solution **/
using System;
using System.Collections.Generic;

namespace PascalTriangle
{
    class Program
    {
        static List<List<int>> GeneratePascalTriangle(int n)
        {
            /**var triangle = List<List<int>>();**/
            List<List<int>> triangle = new List<List<int>>();

            if (n <= 0)
                return triangle;

            for (int i = 0; i < n; i++)
            {
                List<int> row = new List<int> { 1 };
                if (i == 0)
                {
                    triangle.Add(row);
                    continue;
                }
                else
                {
                    List<int> prevRow = triangle[triangle.Count - 1];
                    for (int j = 1; j < i; j++)
                    {
                        int nextValue = prevRow[j - 1] + prevRow[j];
                        row.Add(nextValue);
                    }
                }
                row.Add(1);
                triangle.Add(row);
            }
            return triangle;
        }
    }
}
