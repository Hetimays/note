API
_________________________________________________

Description
+++++++++++++++++++++++++++++++++++++++++++++++++
A load balancer can distribute incoming traffic across your EC2 instances. This enables you to increase the availability of your application. The load balancer also monitors the health of its registered instances and ensures that it routes traffic only to healthy instances. You configure your load balancer to accept incoming traffic by specifying one or more listeners, which are configured with a protocol and port number for connections from clients to the load balancer and a protocol and port number for connections from the load balancer to the instances.

Available Commands
+++++++++++++++++++++++++++++++++++++++++++++++++
tags:
  * `add-tags <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elb/add-tags.html>`_
  * `describe-tags <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elb/describe-tags.html>`_
  * `remove-tags <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elb/remove-tags.html>`_

security-groups-to-load:
  * `apply-security-groups-to-load-balancer <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elb/apply-security-groups-to-load-balancer.html>`_

load-balancer-to:
  * `attach-load-balancer-to-subnets <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elb/attach-load-balancer-to-subnets.html>`_

health:
  * `configure-health-check <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elb/configure-health-check.html>`_

app-cookie-stickiness:
  * `create-app-cookie-stickiness-policy <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elb/create-app-cookie-stickiness-policy.html>`_

lb-cookie-stickiness:
  * `create-lb-cookie-stickiness-policy <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elb/create-lb-cookie-stickiness-policy.html>`_

load-balancer:
  * `create-load-balancer <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elb/create-load-balancer.html>`_
  * `delete-load-balancer <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elb/delete-load-balancer.html>`_
  * `describe-load-balancer-policies <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elb/describe-load-balancer-policies.html>`_

load-balancer-listeners:
  * `create-load-balancer-listeners <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elb/create-load-balancer-listeners.html>`_
  * `delete-load-balancer-listeners <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elb/delete-load-balancer-listeners.html>`_

load-balancer-policy:
  * `create-load-balancer-policy <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elb/create-load-balancer-policy.html>`_
  * `delete-load-balancer-policy <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elb/delete-load-balancer-policy.html>`_
  * `describe-load-balancer-policy-types <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elb/describe-load-balancer-policy-types.html>`_

instances-from-load:
  * `deregister-instances-from-load-balancer <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elb/deregister-instances-from-load-balancer.html>`_

account:
  * `describe-account-limits <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elb/describe-account-limits.html>`_

instance:
  * `describe-instance-health <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elb/describe-instance-health.html>`_

load-balancer-attributes:
  * `describe-load-balancer-attributes <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elb/describe-load-balancer-attributes.html>`_
  * `modify-load-balancer-attributes <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elb/modify-load-balancer-attributes.html>`_

load:
  * `describe-load-balancers <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elb/describe-load-balancers.html>`_

load-balancer-from:
  * `detach-load-balancer-from-subnets <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elb/detach-load-balancer-from-subnets.html>`_

availability-zones-for-load-balancer:
  * `disable-availability-zones-for-load-balancer <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elb/disable-availability-zones-for-load-balancer.html>`_
  * `enable-availability-zones-for-load-balancer <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elb/enable-availability-zones-for-load-balancer.html>`_

instances-with-load:
  * `register-instances-with-load-balancer <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elb/register-instances-with-load-balancer.html>`_

load-balancer-listener-ssl:
  * `set-load-balancer-listener-ssl-certificate <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elb/set-load-balancer-listener-ssl-certificate.html>`_

load-balancer-policies-for-backend:
  * `set-load-balancer-policies-for-backend-server <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elb/set-load-balancer-policies-for-backend-server.html>`_

load-balancer-policies-of:
  * `set-load-balancer-policies-of-listener <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elb/set-load-balancer-policies-of-listener.html>`_

  * `wait <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elb/wait.html>`_




Source
+++++++++++++++++++++++++++++++++++++++++++++++++
https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elb/index.html
