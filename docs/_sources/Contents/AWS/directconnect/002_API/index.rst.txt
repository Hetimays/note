API
_________________________________________________

Description
+++++++++++++++++++++++++++++++++++++++++++++++++
Direct Connect links your internal network to an Direct Connect location over a standard Ethernet fiber-optic cable. One end of the cable is connected to your router, the other to an Direct Connect router. With this connection in place, you can create virtual interfaces directly to the Amazon Web Services Cloud (for example, to Amazon EC2 and Amazon S3) and to Amazon VPC, bypassing Internet service providers in your network path. A connection provides access to all Amazon Web Services Regions except the China (Beijing) and (China) Ningxia Regions. Amazon Web Services resources in the China Regions can only be accessed through locations associated with those Regions.

Available Commands
+++++++++++++++++++++++++++++++++++++++++++++++++
direct-connect-gateway-association-proposal:
  * `accept-direct-connect-gateway-association-proposal <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/accept-direct-connect-gateway-association-proposal.html>`_
  * `create-direct-connect-gateway-association-proposal <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/create-direct-connect-gateway-association-proposal.html>`_
  * `delete-direct-connect-gateway-association-proposal <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/delete-direct-connect-gateway-association-proposal.html>`_

hosted-connection:
  * `allocate-hosted-connection <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/allocate-hosted-connection.html>`_
  * `associate-hosted-connection <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/associate-hosted-connection.html>`_

private-virtual-interface:
  * `allocate-private-virtual-interface <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/allocate-private-virtual-interface.html>`_
  * `confirm-private-virtual-interface <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/confirm-private-virtual-interface.html>`_
  * `create-private-virtual-interface <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/create-private-virtual-interface.html>`_

public-virtual-interface:
  * `allocate-public-virtual-interface <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/allocate-public-virtual-interface.html>`_
  * `confirm-public-virtual-interface <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/confirm-public-virtual-interface.html>`_
  * `create-public-virtual-interface <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/create-public-virtual-interface.html>`_

transit-virtual-interface:
  * `allocate-transit-virtual-interface <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/allocate-transit-virtual-interface.html>`_
  * `confirm-transit-virtual-interface <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/confirm-transit-virtual-interface.html>`_
  * `create-transit-virtual-interface <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/create-transit-virtual-interface.html>`_

connection-with:
  * `associate-connection-with-lag <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/associate-connection-with-lag.html>`_

mac-sec-key:
  * `associate-mac-sec-key <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/associate-mac-sec-key.html>`_
  * `disassociate-mac-sec-key <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/disassociate-mac-sec-key.html>`_

virtual-interface:
  * `associate-virtual-interface <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/associate-virtual-interface.html>`_
  * `delete-virtual-interface <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/delete-virtual-interface.html>`_
  * `update-virtual-interface-attributes <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/update-virtual-interface-attributes.html>`_

connection:
  * `confirm-connection <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/confirm-connection.html>`_
  * `create-connection <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/create-connection.html>`_
  * `delete-connection <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/delete-connection.html>`_
  * `update-connection <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/update-connection.html>`_

customer:
  * `confirm-customer-agreement <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/confirm-customer-agreement.html>`_
  * `describe-customer-metadata <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/describe-customer-metadata.html>`_

bgp-peer:
  * `create-bgp-peer <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/create-bgp-peer.html>`_
  * `delete-bgp-peer <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/delete-bgp-peer.html>`_

direct-connect-gateway:
  * `create-direct-connect-gateway <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/create-direct-connect-gateway.html>`_
  * `delete-direct-connect-gateway <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/delete-direct-connect-gateway.html>`_
  * `describe-direct-connect-gateway-associations <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/describe-direct-connect-gateway-associations.html>`_
  * `describe-direct-connect-gateway-attachments <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/describe-direct-connect-gateway-attachments.html>`_
  * `update-direct-connect-gateway <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/update-direct-connect-gateway.html>`_

direct-connect-gateway-association:
  * `create-direct-connect-gateway-association <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/create-direct-connect-gateway-association.html>`_
  * `delete-direct-connect-gateway-association <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/delete-direct-connect-gateway-association.html>`_
  * `describe-direct-connect-gateway-association-proposals <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/describe-direct-connect-gateway-association-proposals.html>`_
  * `update-direct-connect-gateway-association <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/update-direct-connect-gateway-association.html>`_

interconnect:
  * `create-interconnect <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/create-interconnect.html>`_
  * `delete-interconnect <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/delete-interconnect.html>`_

lag:
  * `create-lag <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/create-lag.html>`_
  * `delete-lag <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/delete-lag.html>`_
  * `update-lag <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/update-lag.html>`_

connections:
  * `describe-connections <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/describe-connections.html>`_

direct-connect:
  * `describe-direct-connect-gateways <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/describe-direct-connect-gateways.html>`_

hosted:
  * `describe-hosted-connections <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/describe-hosted-connections.html>`_

interconnects:
  * `describe-interconnects <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/describe-interconnects.html>`_

lags:
  * `describe-lags <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/describe-lags.html>`_

loa:
  * `describe-loa <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/describe-loa.html>`_

locations:
  * `describe-locations <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/describe-locations.html>`_

router:
  * `describe-router-configuration <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/describe-router-configuration.html>`_

tags:
  * `describe-tags <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/describe-tags.html>`_

virtual:
  * `describe-virtual-gateways <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/describe-virtual-gateways.html>`_
  * `describe-virtual-interfaces <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/describe-virtual-interfaces.html>`_

connection-from:
  * `disassociate-connection-from-lag <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/disassociate-connection-from-lag.html>`_

virtual-interface-test:
  * `list-virtual-interface-test-history <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/list-virtual-interface-test-history.html>`_

bgp-failover-test:
  * `start-bgp-failover-test <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/start-bgp-failover-test.html>`_
  * `stop-bgp-failover-test <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/stop-bgp-failover-test.html>`_

resource:
  * `tag-resource <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/tag-resource.html>`_
  * `untag-resource <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/untag-resource.html>`_





Source
+++++++++++++++++++++++++++++++++++++++++++++++++
https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/index.html
