# ConfigMap

Test creation of objects and features.

* Prepare default test case for kind "ConfigMap"

## Render and Validate
* Render
* Expected number of "7" objects were rendered
* Validate

## Metadata
* Check basic metadata functionality

## Defaulting
* Render
* All test objects have key "data§default_inline_1" with value "Default Inline 1"
* All test objects have key "data§default_file_1.json" with value "\{\"name\":\"i am default_file_1.json\"\}"

* Set test object to "release-name-hull-test-defaults_no_overwrite"
* Test Object has key "data§default_inline_2" with value "Default Inline 2"
* Test Object has key "data§default_file_2.yaml" with value "name: \"i am default_file_2.yaml\""

* Set test object to "release-name-hull-test-defaults_overwrite"
* Test Object has key "data§default_inline_2" with value "Concrete Inline 2"
* Test Object has key "data§default_file_2.yaml" with value "name: \"i am concrete_file_2.yaml\""

## Templating
* Render
* Set test object to "release-name-hull-test-no_templating"
* Test Object has key "data§concrete_file_3_templated.yaml" with value "name: \"i am concrete_file_3.yaml\"\ntemplating: \"General Custom Label 1\""
* Test Object has key "data§concrete_file_3_untemplated.yaml" with value "name: \"i am concrete_file_3.yaml\"\ntemplating: \"\{\{ .Values.hull.config.general.metadata.labels.custom.general_custom_label_1 \}\}\""
* Test Object has key "data§inline_templated.txt" with value "This is an inline with a pointer to a transformation."
* Test Object has key "data§inline_untemplated.txt" with value "This is an inline with a pointer to a \{\{ .Values.hull.config.specific.resolve_me \}\}."


## Transformation
* Render
* Set test object to "release-name-hull-test-transformation_resolved"
* Test Object has key "data§concrete_file_4_resolved.txt" with value "This is a text file with a pointer to a transformation."

___

* Clean the test execution folder