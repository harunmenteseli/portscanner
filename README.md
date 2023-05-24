<h1>Port Scanner</h1>

  <p>
    This is a simple Python script that allows you to scan for open or closed ports on a specific IP address. It utilizes the <code>socket</code> module to establish TCP connections and check the status of individual ports.
  </p>

  <h2>Usage</h2>

  <ol>
    <li>Run the script using a Python interpreter.</li>
    <li>Enter the IP address you want to scan when prompted.</li>
    <li>Enter the starting and ending port numbers to define the port range you wish to scan.</li>
  </ol>

  <p>
    The script will then iterate over the specified port range and display whether each port is open or closed.
  </p>

  <h2>Example</h2>

  <pre>
Enter IP Address: 192.168.0.1
Enter start port: 1
Enter end port: 100

1 port is closed.
2 port is closed.
3 port is closed.
...
80 port number is open.
81 port is closed.
...
100 port is closed.
  </pre>

  <p>
    Please note that the script uses a timeout of 5 seconds when attempting to establish a connection to each port. You can modify this value by adjusting the <code>s.settimeout(5)</code> line in the code.
  </p>

  <p>
    <strong>Disclaimer:</strong> Port scanning without proper authorization may violate the terms of service of the target system or network. Make sure to obtain proper permissions before using this script on any system or network you do not own or operate.
  </p>
