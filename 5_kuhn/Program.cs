using System;
using System.Collections;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Xml.Serialization;

namespace kuhn
{
    class Program
    {
        private static (Dictionary<string, List<string>> graph, List<string> Y) ParseFile(string filename)
        {
            var lines = File.ReadAllLines(filename);
            var Y = new HashSet<string>();
            var graph = new Dictionary<string, List<string>>();
            for (var i = 1; i < lines.Length; i++)
            {
                var elements = lines[i].Split(' ').Where(x => x != "0");
                graph.Add(i.ToString(), new List<string>(elements));
                foreach (var el in elements)
                    Y.Add(el);
            }
            return (graph, Y.ToList());
        }

        private static (bool, Dictionary<string, string> matchings) KuhnAlgo(Dictionary<string, string> matchings, Dictionary<string, List<string>> graph)
        {
            var X = graph.Keys.ToList();
            var visited = graph.Keys.ToDictionary(key => key, key => new List<string>());
            var indication = 1;

            while (indication != 0 && X.Count != 0)
            {
                var stack = new Stack<string>();
                stack.Push(X[0]);

                indication = 0;
                while (stack.Count != 0 && indication == 0)
                {
                    var x = stack.Peek();
                    var y = Choice(x, visited, graph);

                    if (y != "")
                    {
                        stack.Push(y);
                        var z = matchings[y];
                        if (z != "")
                            stack.Push(z);
                        else
                            indication = 1;
                    }
                    else
                    {
                        stack.Pop();
                        if (stack.Count != 0)
                            stack.Pop();
                    }
                }
                if (indication == 1) {
                    while (stack.Count != 0)
                    {
                        var y = stack.Pop();
                        var x = stack.Pop();
                        X.Remove(x);
                        matchings[y] = x;
                    }
                }
            }

            if (indication == 0 || X.Count != 0)
                return (false, matchings);
            return (true, matchings);
        }

        private static string Choice(string x, Dictionary<string, List<string>> visited, Dictionary<string, List<string>> graph)
        {
            foreach (var vert in graph[x])
            {
                if (visited[x].Contains(vert)) continue;
                visited[x].Add(vert);
                return vert;
            }
            return "";
        }
        
        static void Main(string[] args)
        {
            var (graph, Y) = ParseFile("in.txt");
            var emptyMatchings = Y.ToDictionary(el => el, el => "");

            var (isMatchingsExist, matchings) = KuhnAlgo(emptyMatchings, graph);

            WriteResultToFile(isMatchingsExist, matchings, "out.txt");

        }

        private static void WriteResultToFile(bool isMatchingsExist, Dictionary<string, string> matchings, string filename)
        {
            var SW = new StreamWriter(new FileStream(
                filename,
                FileMode.Create,
                FileAccess.Write));

            if (!isMatchingsExist)
                SW.Write("N");
            else
                SW.Write("Y\n" + 
                         string.Join(" ", matchings.OrderBy(pair => pair.Value)
                             .ToDictionary(pair => pair.Key, pair => pair.Value).Keys));
            SW.Close();    
        }
    }
}