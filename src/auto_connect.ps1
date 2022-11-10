$command = "start ceclient.exe --auto-connect"
Invoke-Expression($command)

# Use -h or --help argument to check the valid arguments
# start ceclient.exe --help
#
# Use -ac or --auto-connect to connect automatically to the last connected server
# start ceclient.exe --auto-connect
#
# Use -ip or --ip argument to specify a static IP Address
# start ceclient.exe --auto-connect --ip [ip]
#
# Use -sn or --server-name to specify a server name from server list
# start ceclient.exe --auto-connect --server-name [server_name]
