An Dynamic DNS provider written in Python.

In simple terms this is a couple of HTTP endpoints to accept update requests to Dynamic DNS providers that routers typically send. All requests will ultimately do the same as they’re just different to allow for better compatiblity.

## Usage

As a command-line parameter you pass what should be done when the endpoint was called—when the router announce a new possibly new public IP address.

```
./ddns-endpoint.py update_a_record.py
```

`update_a_record.py` could be a script that updates a DNS A record with the new public IP address.
