using System;
using System.Net;
using System.Diagnostics;
using KRPC;
using KRPC.Service;
using KRPC.Utils;

namespace TestServer
{
    class MainClass
    {
        public static void Main (string[] args)
        {
            Logger.Enabled = true;
            Logger.Level = Logger.Severity.Warning;
            const int frameTime = 50;
            var server = new KRPCServer (IPAddress.Loopback, ushort.Parse (args [0]), ushort.Parse (args [1]));
            KRPCServer.Context.SetGameScene (GameScene.SpaceCenter);
            var timeSpan = new TimeSpan ();
            server.GetUniversalTime = () => timeSpan.TotalSeconds;
            server.OnClientRequestingConnection += (s, e) => e.Request.Allow ();
            server.Start ();
            Logger.WriteLine ("Started test server...");
            while (server.Running) {
                Stopwatch timer = Stopwatch.StartNew ();
                server.Update ();
                var elapsed = timer.ElapsedMilliseconds;
                var sleep = frameTime - elapsed;
                if (sleep > 0)
                    System.Threading.Thread.Sleep ((int)sleep);
            }
            Logger.WriteLine ("Test server stopped");
        }
    }
}
