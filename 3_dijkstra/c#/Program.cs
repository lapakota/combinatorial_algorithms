using System;
using System.Collections.Generic;
using System.IO;

namespace dijkstra
{
    class Program
    {
        class Graph
        {
            public int vertCount;
            public int[,] adjMatrix;

            public Graph(string[] content, int vertCount)
            {
                this.vertCount = vertCount;
                this.adjMatrix = CreateGraph(content, vertCount);
            }

            private int[,] MemSet(int[,] arr, int val)
            {
                for (var i = 0; i < this.vertCount; i++)
                    for (var j = 0; j < this.vertCount; j++)
                        arr[i, j] = val;
                return arr;
            }

            private int[] MemSet(int[] arr, int val)
            {
                for (var i = 0; i < this.vertCount; i++)
                    arr[i] = val;
                return arr;
            }

            private int[,] CreateGraph(string[] content, int vertCount)
            {
                var adjMatrix = MemSet(new int[vertCount, vertCount], -1);

                for (var i = 1; i <= vertCount; i++)
                {
                    var splitedStr = content[i].Split(" ");
                
                    for (var j = 0; j < splitedStr.Length - 1; j += 2)
                    {
                        var previousVertex = int.Parse(splitedStr[j]);
                        var vertex = i;
                        var weight = int.Parse(splitedStr[j + 1]);

                        adjMatrix[previousVertex - 1, vertex - 1] = weight;
                    }
                }
                
                return adjMatrix;
            }

            private int GetMinVertex(bool[] visited, int[] distance)
            {
                var minKey = int.MaxValue;
                var vertex = -1;
                for (var i = 0; i < this.vertCount; i++)
                {
                    if (!visited[i] && minKey > distance[i])
                    {
                        minKey = distance[i];
                        vertex = i;
                    }
                }
                return vertex;
            }

            public Tuple<int[], int[]> Dijkstra(int start)
            {
                var visited = new bool[this.vertCount];
                var distance = MemSet(new int[this.vertCount], int.MaxValue);
                var prev = new int[this.vertCount];

                distance[start - 1] = 0;
                for (var i = 0; i < this.vertCount; i++)
                {
                    var vertex = GetMinVertex(visited, distance);

                    if (vertex == -1)
                        continue;

                    visited[vertex] = true;
                    for (var adjVertex = 0; adjVertex < this.vertCount; adjVertex++)
                    {
                        if (this.adjMatrix[vertex, adjVertex] >= 0 && !visited[adjVertex]) {
                            var newKey = this.adjMatrix[vertex, adjVertex] + distance[vertex];

                            if (newKey < distance[adjVertex])
                            {
                                distance[adjVertex] = newKey;
                                prev[adjVertex] = vertex + 1;
                            }
                        }
                    }
                }

                return new Tuple<int[], int[]>(distance, prev);
            }

            public string GetRoute(int[] distance, int[] prev, int start, int end)
            {
                var dist = distance[end - 1];

                if (dist == int.MaxValue)
                    return "N";
                var vertex = end;
                var output = end.ToString() + " ";

                for (var i = 0; i < this.vertCount; i++)
                {
                    vertex = prev[vertex - 1];
                    output += vertex.ToString() + " ";
                    if (vertex == start)
                        break;
                }
                var outputArr = output.Split(" ");
                Array.Reverse(outputArr);
                return "Y\n" + String.Join(" ", outputArr).Substring(1) + "\n" + dist;
            }
        }

        class FileParser
        {
            public static Tuple<Graph, int, int> ParseData(string fileName)
            {
                using StreamReader file = new StreamReader(fileName);
                var content = file.ReadToEnd().Split("\n");
                var vertCount = int.Parse(content[0].ToString());

                var start = int.Parse(content[content.Length - 2]);
                var end = int.Parse(content[content.Length - 1]);
                var graph = new Graph(content, vertCount);

                return new Tuple<Graph, int, int>(graph, start, end);
            }
        }


        static void Main()
        {
            var data = FileParser.ParseData("in.txt");
            var graph = data.Item1;
            var start = data.Item2;
            var end = data.Item3;

            var dijkstraRes = graph.Dijkstra(start);

            var distance = dijkstraRes.Item1;
            var prev = dijkstraRes.Item2;

            var answer = graph.GetRoute(distance, prev, start, end);

            var SW = new StreamWriter(new FileStream(
                "out.txt",
                FileMode.Create,
                FileAccess.Write));

            SW.Write(answer);
            SW.Close();

        }
    }
}
