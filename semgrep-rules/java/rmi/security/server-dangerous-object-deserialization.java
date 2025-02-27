// cf. https://mogwailabs.de/blog/2019/03/attacking-java-rmi-services-after-jep-290/

package de.mogwailabs.BSidesRMIService;

import java.rmi.Naming;
import java.rmi.registry.LocateRegistry;

import java.rmi.Remote;
import java.rmi.RemoteException;

// ruleid:server-dangerous-object-deserialization
public interface IBSidesService extends Remote {
   boolean registerTicket(String ticketID) throws RemoteException;
   void vistTalk(String talkID) throws RemoteException;
   void poke(Object attende) throws RemoteException;
}

// ruleid:server-dangerous-object-deserialization
public interface IBSidesService extends Remote {
   boolean registerTicket(String ticketID) throws RemoteException;
   void vistTalk(String talkID) throws RemoteException;
   void poke(StringBuilder attende) throws RemoteException;
}

// ok:server-dangerous-object-deserialization
public interface IBSidesServiceOK extends Remote {
   boolean registerTicket(String ticketID) throws RemoteException;
   void vistTalk(String talkID) throws RemoteException;
   void poke(int attende) throws RemoteException;
}

// ok:server-dangerous-object-deserialization
public interface IBSidesServiceOK extends Remote {
   boolean registerTicket(String ticketID) throws RemoteException;
   void vistTalk(String talkID) throws RemoteException;
   void poke(Integer attende) throws RemoteException;
}

public class BSidesServer {
    public static void main(String[] args) {
        try {
            // Create new RMI registry to which we can register
            LocateRegistry.createRegistry(1099);

            // Make our BSides Server object
            // available under the name "bsides"
            Naming.bind("bsides", new BSidesServiceServerImpl());
            System.out.println("BSides RMI server is ready");

        } catch (Exception e) {
            // In case of an error, print the stacktrace
            // and bail out
            e.printStackTrace();
        }
    }
}
