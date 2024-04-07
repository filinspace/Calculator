#!/bin/bash

run_ping_traceroute_and_certificate_info() {
    host=$1

    # Get client information
    client_info="Client Information:
IP: $(curl -s ipinfo.io/ip)
Region: $(curl -s ipinfo.io/region)
Country: $(curl -s ipinfo.io/country)
Model: $(uname -m)
Provider: $(curl -s ipinfo.io/org)"

    # Perform ping and traceroute
    result=$(ping -c 4 $host && traceroute $host)

    # Get certificate information
    certificate_info=$(openssl s_client -connect $host:443 </dev/null 2>/dev/null | openssl x509 -noout -subject -issuer -dates)

    # Save results to text file
    filename="pingtrace_${host}.txt"
    echo "$client_info" > "$filename"
    echo "" >> "$filename"
    echo "---------- Ping and Traceroute ----------" >> "$filename"
    echo "$result" >> "$filename"
    echo "" >> "$filename"
    echo "---------- Certificate Information ----------" >> "$filename"
    echo "$certificate_info" >> "$filename"

    echo "Results saved to $filename."
}

# Greet user before asking for the URL host
echo -n "Enter the URL host: "
# Read URL host input from user
read host

# Display message after entering URL host
echo "Processing. Please wait..."

# Execute ping, traceroute, certificate info retrieval, and client info retrieval
run_ping_traceroute_and_certificate_info $host >/dev/null 2>&1 && echo "All done."
