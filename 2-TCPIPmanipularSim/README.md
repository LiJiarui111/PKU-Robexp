# 2-TCPIPmanipulatorSim

## How to use
Run `tcp_client.py`, and the client will automatically send velocity control commands to the server at 2Hz (you can change the frequency by editing the sleeping time), which is the 
URSim software running in the virtual machine. 

The IP address of the server should be modified when needed, and also you should guarantee that the client and server
can build up communications successfully in a network, but this is satisfied automatically when using the virtual machine. 
