# This module is automatically generated by autogen.sh. DO NOT EDIT.

from . import _DigitalOcean


class _Network(_DigitalOcean):
    _type = "network"
    _icon_dir = "resources/digitalocean/network"


class Certificate(_Network):
    _icon = "certificate.png"


class DomainRegistration(_Network):
    _icon = "domain-registration.png"


class Domain(_Network):
    _icon = "domain.png"


class Firewall(_Network):
    _icon = "firewall.png"


class FloatingIp(_Network):
    _icon = "floating-ip.png"


class InternetGateway(_Network):
    _icon = "internet-gateway.png"


class LoadBalancer(_Network):
    _icon = "load-balancer.png"


class ManagedVpn(_Network):
    _icon = "managed-vpn.png"


class Vpc(_Network):
    _icon = "vpc.png"


# Aliases
