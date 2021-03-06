using System;
using System.Net;
using System.Net.Sockets;

namespace KRPC.Server.Net
{
    sealed class TCPClient : IClient<byte,byte>
    {
        readonly Guid guid;
        readonly TcpClient tcpClient;

        public TCPClient (TcpClient tcpClient)
        {
            guid = Guid.NewGuid ();
            this.tcpClient = tcpClient;
            try {
                var remoteEndPoint = tcpClient.Client.RemoteEndPoint as IPEndPoint;
                Address = remoteEndPoint.Address.ToString ();
            } catch {
                Address = "";
            }
        }

        public string Name {
            get { return Guid.ToString (); }
        }

        public Guid Guid {
            get { return guid; }
        }

        public string Address { get; private set; }

        public IStream<byte,byte> Stream {
            get {
                try {
                    return new TCPStream (tcpClient.GetStream ());
                } catch (ObjectDisposedException) {
                    throw new ClientDisconnectedException ();
                } catch (InvalidOperationException) {
                    throw new ClientDisconnectedException ();
                }
            }
        }

        public bool Connected {
            get {
                try {
                    if (!tcpClient.Client.Connected) {
                        return false;
                    }
                    if (tcpClient.Client.Poll (0, SelectMode.SelectRead)) {
                        var buffer = new byte[1];
                        return tcpClient.Client.Receive (buffer, SocketFlags.Peek) != 0;
                    }
                    return true;
                } catch {
                    return false;
                }
            }
        }

        public void Close ()
        {
            tcpClient.Close ();
        }

        public override bool Equals (Object obj)
        {
            return obj != null && Equals (obj as TCPClient);
        }

        public bool Equals (IClient<byte,byte> other)
        {
            if ((object)other == null)
                return false;
            var otherClient = other as TCPClient;
            if ((object)otherClient == null)
                return false;
            return guid == otherClient.guid;
        }

        public override int GetHashCode ()
        {
            return guid.GetHashCode ();
        }

        public static bool operator == (TCPClient lhs, TCPClient rhs)
        {
            if (Object.ReferenceEquals (lhs, rhs))
                return true;
            if ((object)lhs == null || (object)rhs == null)
                return false;
            return lhs.Equals (rhs);
        }

        public static bool operator != (TCPClient lhs, TCPClient rhs)
        {
            return !(lhs == rhs);
        }
    }
}

