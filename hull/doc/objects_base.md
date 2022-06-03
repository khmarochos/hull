# Base properties for all objects

The following configuration properties are available to all objects specified via HULL.

## JSON Schema Elements

### The `hull.ObjectBase.v1` properties

You can add the following optional properties to any object specified via HULL: 

| Parameter | Description  | Default | Example 
| --------  | -------------| ------- | --------
`staticName` | A boolean switch. If set to true the object does not get a dynamically created name (see above) assigned but a name that only consists of the key name. Using static names is helpful in case you need to address the object from another Kubernetes object that is not part of the Helm chart and hence you want to refer to particular object in the cluster by a fixed name. Note that by setting `hull.config.general.noObjectNamePrefixes` to `true`, the individual `staticName` settings have no effect anymore | `false` | `true`<br>`false`
`enabled` | Needs to resolve to a boolean switch, it can be a boolean input directly or a transformation that resolves to a boolean value. If resolved to true or missing, the object will be rendered for deployment. If resolved to false, it will be omitted. This way you can predefine objects which are only enabled and created in the cluster in certain environments when needed. | `true` | `true`<br>`false`<br><br>`"_HULL_TRANSFORMATION_<<<NAME=hull.util.transformation.tpl>>><<<CONTENT=`<br>&#160;&#160;`{{`&#160;`(index`&#160;`.`&#160;`\"PARENT\").Values.hull.config.specific.enable_addon`&#160;`}}>>>"`
`annotations` | Dictionary with annotations to add to the Kubernetes objects main `metadata.annotations` section | `{}` | `appImportance:`&#160;`"very`&#160;`low"`
`labels` | Dictionary with labels to add to the Kubernetes objects main `metadata.labels` section. | `{}` | `appStatus:`&#160;`"good"`

---
Back to [README.md](./../README.md)
