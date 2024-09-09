API
_________________________________________________

Description
+++++++++++++++++++++++++++++++++++++++++++++++++
Lambda is a compute service that lets you run code without provisioning or managing servers. Lambda runs your code on a high-availability compute infrastructure and performs all of the administration of the compute resources, including server and operating system maintenance, capacity provisioning and automatic scaling, code monitoring and logging. With Lambda, you can run code for virtually any type of application or backend service. For more information about the Lambda service, see What is Lambda in the Lambda Developer Guide .

Available Commands
+++++++++++++++++++++++++++++++++++++++++++++++++
layer-version-permission:
  * `add-layer-version-permission <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/add-layer-version-permission.html>`_
  * `remove-layer-version-permission <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/remove-layer-version-permission.html>`_

permission:
  * `add-permission <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/add-permission.html>`_
  * `remove-permission <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/remove-permission.html>`_

alias:
  * `create-alias <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/create-alias.html>`_
  * `delete-alias <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/delete-alias.html>`_
  * `get-alias <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/get-alias.html>`_
  * `update-alias <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/update-alias.html>`_

code-signing-config:
  * `create-code-signing-config <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/create-code-signing-config.html>`_
  * `delete-code-signing-config <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/delete-code-signing-config.html>`_
  * `get-code-signing-config <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/get-code-signing-config.html>`_
  * `update-code-signing-config <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/update-code-signing-config.html>`_

event-source-mapping:
  * `create-event-source-mapping <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/create-event-source-mapping.html>`_
  * `delete-event-source-mapping <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/delete-event-source-mapping.html>`_
  * `get-event-source-mapping <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/get-event-source-mapping.html>`_
  * `update-event-source-mapping <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/update-event-source-mapping.html>`_

function:
  * `create-function <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/create-function.html>`_
  * `delete-function <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/delete-function.html>`_
  * `get-function <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/get-function.html>`_
  * `update-function-code <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/update-function-code.html>`_

function-url-config:
  * `create-function-url-config <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/create-function-url-config.html>`_
  * `delete-function-url-config <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/delete-function-url-config.html>`_
  * `get-function-url-config <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/get-function-url-config.html>`_
  * `update-function-url-config <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/update-function-url-config.html>`_

function-code-signing-config:
  * `delete-function-code-signing-config <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/delete-function-code-signing-config.html>`_
  * `get-function-code-signing-config <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/get-function-code-signing-config.html>`_
  * `put-function-code-signing-config <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/put-function-code-signing-config.html>`_

function-concurrency:
  * `delete-function-concurrency <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/delete-function-concurrency.html>`_
  * `get-function-concurrency <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/get-function-concurrency.html>`_
  * `put-function-concurrency <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/put-function-concurrency.html>`_

function-event-invoke-config:
  * `delete-function-event-invoke-config <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/delete-function-event-invoke-config.html>`_
  * `get-function-event-invoke-config <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/get-function-event-invoke-config.html>`_
  * `put-function-event-invoke-config <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/put-function-event-invoke-config.html>`_
  * `update-function-event-invoke-config <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/update-function-event-invoke-config.html>`_

layer-version:
  * `delete-layer-version <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/delete-layer-version.html>`_
  * `get-layer-version <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/get-layer-version.html>`_
  * `get-layer-version-policy <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/get-layer-version-policy.html>`_
  * `publish-layer-version <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/publish-layer-version.html>`_

provisioned-concurrency-config:
  * `delete-provisioned-concurrency-config <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/delete-provisioned-concurrency-config.html>`_
  * `get-provisioned-concurrency-config <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/get-provisioned-concurrency-config.html>`_
  * `put-provisioned-concurrency-config <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/put-provisioned-concurrency-config.html>`_

account:
  * `get-account-settings <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/get-account-settings.html>`_

function-configuration:
  * `get-function-configuration <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/get-function-configuration.html>`_
  * `update-function-configuration <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/update-function-configuration.html>`_

function-recursion-config:
  * `get-function-recursion-config <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/get-function-recursion-config.html>`_
  * `put-function-recursion-config <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/put-function-recursion-config.html>`_

layer-version-by:
  * `get-layer-version-by-arn <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/get-layer-version-by-arn.html>`_

policy:
  * `get-policy <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/get-policy.html>`_

runtime-management-config:
  * `get-runtime-management-config <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/get-runtime-management-config.html>`_
  * `put-runtime-management-config <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/put-runtime-management-config.html>`_

aliases:
  * `list-aliases <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/list-aliases.html>`_

code-signing:
  * `list-code-signing-configs <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/list-code-signing-configs.html>`_

event-source:
  * `list-event-source-mappings <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/list-event-source-mappings.html>`_

function-event-invoke:
  * `list-function-event-invoke-configs <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/list-function-event-invoke-configs.html>`_

function-url:
  * `list-function-url-configs <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/list-function-url-configs.html>`_

functions:
  * `list-functions <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/list-functions.html>`_

functions-by-code-signing:
  * `list-functions-by-code-signing-config <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/list-functions-by-code-signing-config.html>`_

layer:
  * `list-layer-versions <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/list-layer-versions.html>`_

layers:
  * `list-layers <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/list-layers.html>`_

provisioned-concurrency:
  * `list-provisioned-concurrency-configs <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/list-provisioned-concurrency-configs.html>`_

tags:
  * `list-tags <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/list-tags.html>`_

versions-by:
  * `list-versions-by-function <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/list-versions-by-function.html>`_

version:
  * `publish-version <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/publish-version.html>`_

resource:
  * `tag-resource <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/tag-resource.html>`_
  * `untag-resource <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/untag-resource.html>`_

  * `invoke <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/invoke.html>`_
  * `wait <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/wait.html>`_
  * `wizard <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/wizard.html>`_




Source
+++++++++++++++++++++++++++++++++++++++++++++++++
https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/index.html
