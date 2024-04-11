Article

# Configuring Entities

Model your app’s objects.

## Overview

An entity describes an object, including its name, attributes, and
relationships. Create an entity for each of your app’s objects.

### Add Entities

After you create a Core Data model as described in Creating a Core Data model,
add an entity to your project’s `.xcdatamodeld` file:

  1. Click Add Entity at the bottom of the editor area. A new entity with placeholder name `Entity` appears in the Entities list.

  2. In the Entities list, double-click the newly added entity and rename it. This step updates both the entity name and class name visible in the Data Model inspector.

In addition to the required name and class name fields, entities have a
default setting for the required code generation field. If you need to add
inheritance, unique constraints, versioning, or other optional information,
configure your entity as described below. Otherwise, add the properties that
compose your entity as described in Configuring Attributes.

### Configure Entities

Use the data model inspector (choose View > Inspectors > Show Data Model
Inspector) to configure your entity.

Entity Name

    

The name of the entity in the managed object model. This field reflects the
name shown in the Entities list.

Abstract Entity

    

Select the Abstract Entity checkbox if you won’t create any instances of the
entity—for example, if it exists only as a parent entity that must never be
instantiated directly. By default, this option is unselected, resulting in a
concrete entity.

Parent Entity

    

If you have a number of similar entities, you can define the common properties
in a parent entity, and have child entities inherit those properties. By
default, this field is blank.

Class Name

    

The name of the class you'll use when creating managed object instances from
this entity. By default, the class name mirrors the entity name; however, if
you change the class name, the entity name doesn’t reflect the changes.

Module

    

The module where the class for this entity resides. By default, Core Data
locates class files in the global namespace.

Codegen

    

Choose a code generation option for generating managed object subclass and
properties files to support your entity. By default, this option is set to
Class Definition, and Core Data generates both files for you automatically.

For information about the options for code generation, see Generating code.

Constraints

    

After adding attributes as shown in Configuring Attributes, optionally enter
the name of an attribute (or comma-separated list of attributes) to serve as
unique constraints on the entity.

Unique constraints prevent duplicate records in the store. When saving a new
record, the store checks whether any record already exists with the same value
for the constrained attribute. In the case of a conflict,
`NSMergePolicyType.mergeByPropertyObjectTrumpMergePolicyType` causes the new
record to overwrite all fields in the existing record.

Spotlight Display Name

    

An `NSExpression` that Core Spotlight uses to display an instance of this
entity. This expression may include keypaths, language functions like
`lowercased()` and `uppercased()`, and custom functions.

For more information, see Core Spotlight.

User Info

    

A dictionary in which you can optionally store any application-specific
information related to the entity.

Versioning Hash Modifier

    

Provide a hash modifier when maintaining multiple model versions if the
structure of an entity is the same, but the format or content of its data has
changed.

Versioning Renaming ID

    

Provide a renaming ID if you rename an entity between model versions. Set the
renaming identifier in the new model to the name of the corresponding entity
in the previous model.

For more information, see Migrating your data model automatically.

## See Also

### Configuring a Core Data Model

Configuring Attributes

Describe the properties that compose an entity.

Configuring Relationships

Specify how entities relate and how change propagates between them.

Generating code

Automatically or manually generate managed object subclasses from entities.

Article

# Configuring Attributes

Describe the properties that compose an entity.

## Overview

After you create an entity as described in Configuring Entities, you can add
attributes to that entity.

An attribute describes a property of an entity. At minimum, you need to
specify the property’s name and data type, whether it must be saved in the
store, and whether it’s required to have a value when it’s saved.

For some attribute types, you can also choose whether to use a scalar type to
represent the attribute in generated classes, as well as configure the
attribute to have a default value, or to apply data validation rules.

### Add Attributes

Add an attribute as indicated in the screenshot and the steps that follow:

  1. With an entity selected, click Add Attribute at the bottom of the editor area. A new attribute with the placeholder name `attribute`, of type `Undefined`, appears in the Attributes list.

  2. In the Attributes list, double-click the newly added attribute, and rename it.

  3. In the Attributes list, as shown in the second screenshot, click `Undefined` and choose the attribute’s data type from the Type pop-up menu.

### Configure Attributes

Use the data model inspector (choose View > Inspectors > Show Data Model
Inspector) to configure attributes.

Attribute Type

    

The attribute’s data type. This field reflects the selection made in the
Attributes list’s Type pop-up menu.

For the full list of types, see `NSAttributeType`.

Optional

    

Optional attributes aren’t required to have a value when saved to the
persistent store. Attributes are optional by default.

Core Data optionals aren’t the same as Swift optionals. You can use a Swift
optional to represent a required attribute, for example, if you need
flexibility to set its value during the time between the object’s
initialization and its first save.

Transient

    

Transient attributes aren’t saved to the persistent store. By default,
attributes are saved to the store. Transient attributes are a useful place to
temporarily store calculated or derived values. Core Data does track changes
to transient property values for undo purposes.

Allows Cloud Encryption

    

For persistent stores that write to a CloudKit database, this option instructs
the system to encrypt the attribute’s value before it’s sent to iCloud. For
more information, see `allowsCloudEncryption`.

Default Value

    

Most types allow you to supply a default value. New object instances set the
attribute to this default value on initialization, unless you specify another
value at that time.

Supplying a default value, in combination with making the type non-optional,
can provide performance benefits.

Use Scalar Type

    

Optionally, for some types, choose between scalar and nonscalar
representations during code generation. For a `Double`, selecting the Use
Scalar checkbox produces a `Double`, while leaving it unselected produces an
`NSNumber`.

For the full list of types, including scalar variants, see `NSAttributeType`.

Validation

    

Optionally, set validation rules, such as the minimum and maximum values for a
numeric type, or regular expressions requirements for strings. The data model
inspector shows validation options specific to the selected attribute’s type.

Index in Spotlight

    

Adds the field to the Spotlight index for instances created from this entity.

For more information, see Core Spotlight.

Preserve After Deletion

    

Includes the attribute in this entity’s tombstone. When persistent history
tracking is enabled and a context deletes a managed object, Core Data records
an identifying marker, known as its tombstone, in the relevant transaction.

User Info

    

A dictionary in which you can store any application-specific information
related to the attribute.

Versioning Hash Modifier

    

Provide a hash modifier when maintaining multiple model versions if the
structure of an attribute is the same, but the format or content of its data
has changed.

Versioning Renaming ID

    

If you rename an attribute between model versions, set the renaming identifier
in the new model to the name of the corresponding attribute in the previous
model.

For more information, see Migrating your data model automatically.

## See Also

### Configuring a Core Data Model

Configuring Entities

Model your app’s objects.

Configuring Relationships

Specify how entities relate and how change propagates between them.

Generating code

Automatically or manually generate managed object subclasses from entities.

Article

# Configuring Relationships

Specify how entities relate and how change propagates between them.

## Overview

After you define at least two entities as described in Configuring Entities,
you can add a relationship between the entities.

A relationship describes how an entity affects another entity. At minimum, a
relationship specifies a name, a destination entity, a delete rule, a
cardinality type (To One or To Many), settings for whether the relationship
must be saved in the store (transient), and whether it is required to have a
value when saved (optional). You must also configure every relationship with
an inverse relationship.

### Add Relationships

To add a relationship, do the following:

  1. Select the graph editor style to view all your app’s entities.

  2. Control-drag from one entity to another to create a pair of relationships. An arrow appears between the entities to indicate a relationship, and the editor creates a placeholder relationship with the name `newRelationship` in each entity.

### Configure Relationships

After creating a pair of relationships, configure each relationship as
indicated in the screenshot and the steps that follow:

  1. Select the table editor style to edit one entity at a time.

  2. Open the Data Model inspector (choose View > Inspectors > Show Data Model Inspector). 

  3. Select the source entity from the Entities list, then select the new relationship in the Relationships list. Use the Data Model inspector to configure its name, destination, inverse, delete rule, and cardinality type, and to indicate if it is transient or optional.

  4. Select the destination entity from the Entities list, then select the new relationship in the Relationships list. Use the Data Model inspector to configure its name, destination, inverse, delete rule, and cardinality type, and to indicate if it is transient or optional.

The above example shows a `Quake` entity’s `countries` relationship, referring
to one or more countries a given earthquake affects. It has an inverse
relationship on the `Country` entity called `quakes`, referring to any
earthquakes affecting that country.

Transient

    

Transient relationships aren’t saved to the persistent store. So transient
relationships are useful to temporarily store calculated or derived values.
Core Data does track changes to transient property values for undo purposes.

Optional

    

Optional relationships aren’t required to have any instances of their
destination type. A required relationship must point to one or more instances
of the destination type.

Destination

    

Each relationship points from a source entity (the entity whose relationships
you’re editing) to a destination entity. The destination entity is a related
type that affects and is affected by the source type.

Setting the same source and destination types creates a reflexive
relationship. For example, an `Employee` may manage another `Employee`.

Inverse

    

Inverse relationships enable Core Data to propagate change in both directions
when an instance of either the source or destination type changes. Every
relationship must have an inverse.

When creating relationships in the Graph editor, you add inverse relationships
between entities in a single step. When creating relationships in the Table
editor, you add inverse relationships to each entity individually.

Delete Rule

    

A relationship’s delete rule specifies how changes propagate across
relationships when Core Data deletes a source instance.

Select No Action to delete the source object instance, but leave references to
it in any destination object instances, which you update manually.

Select**** Nullify to delete the source object instance, and nullify
references to it in any destination object instances.

Select Cascade to delete the source object instance, and with it, all of the
destination object instances.

Select Deny to delete the source object only if it doesn’t point to any
destination object instances.

Cardinality Type

    

Specify a relationship as being To One or To Many, which is known as its
cardinality.

Use To One relationships to connect the source with a single instance of the
destination type.

Use To Many relationships to connect the source with a mutable set of the
destination type, and to optionally specify an arrangement and count:

Arrangement—Select the Ordered checkbox to specify that the relationship has
an inherent ordering, and to generate an _ordered_ mutable set.

Count—You can also place upper and lower limits on the number of destination
instances. For optional relationships, the number of instances can be zero or
within these bounds.

Index in Spotlight

    

Includes the field in the Spotlight index. For more information, see Core
Spotlight.

## See Also

### Configuring a Core Data Model

Configuring Entities

Model your app’s objects.

Configuring Attributes

Describe the properties that compose an entity.

Generating code

Automatically or manually generate managed object subclasses from entities.

### Related Documentation

`enum NSDeleteRule`

Constants that determine what happens when you delete a relationship’s owning
managed object.

Article

# Generating code

Automatically or manually generate managed object subclasses from entities.

## Overview

After you define your entities, their attributes, and relationships as
described in Configuring a Core Data Model, specify the classes that you’ll
use to create instances of your entities. Core Data optionally generates two
files to support your class: a class file and a properties file.

The class file declares the class as a subclass of `NSManagedObject`:

The properties file declares an extension to hold the `@NSManaged` properties
that represent attributes and relationships, their accessors, and helper
functionality for fetching instances of this type:

Core Data takes care of generating managed object subclasses for you, but you
can take control when you need to add logic or edit properties.

### Select a Code Generation Option

To select a code generation option:

  1. Select an entity from the Entities list. 

  2. In the Data Model inspector, below Class, the Codegen pop-up menu offers three options: Manual/None, Class Definition, and Category/Extension. 

The sections that follow describe circumstances for choosing each option.

#### Automatically Generate Both Files

Choose Class Definition when you don’t need to edit the properties or
functionality of the managed object subclass and properties files that Core
Data generates for you.

The generated source code doesn’t appear in your project’s source list. Xcode
produces the class and properties files as part of the build process and
places them in your project’s build directory.

These files regenerate whenever the related entity changes in the data model.

#### Generate the Properties File Only

Choose Category/Extension to add additional convenience methods or business
logic inside your managed object subclass.

This option allows you take full control of the class file, while continuing
to automatically generate the properties file to keep it up-to-date with the
model editor. It’s up to you to create and maintain your class manually.

To generate the class file initially, do the following:

  1. From the Xcode menu bar, choose Editor > Create NSManagedObject Subclass.

  2. Select your data model, then the appropriate entity, and choose where to save the files. Xcode places both class and properties files into your project. 

  3. Because the build process continues to generate the properties file, move this duplicate file from your project source list to the Trash.

You can now see and edit the class file in your project source list.

#### Manage Both Files Manually

Choose Manual/None to edit the properties in your managed object subclass, for
example, to alter access modifiers, and to add additional convenience methods
or business logic.

Using this option, Core Data doesn’t generate any files to support your
managed object. You create and maintain your class, including its properties,
manually. Core Data then locates these files using the values you supply in
the class name and module fields.

To generate the class and properties files initially:

  1. From the Xcode menu bar, choose Editor > Create NSManagedObject Subclass.

  2. Select your data model, then the appropriate entity, and choose where to save the files. Xcode places both a class and a properties file into your project.

You can now see and edit both the class and properties files in your project
source list.

Note

To regenerate class and properties files at any time, choose Editor > Create
NSManagedObject Subclass. Be aware that the new files overwrite any existing
files at the target location.

## See Also

### Configuring a Core Data Model

Configuring Entities

Model your app’s objects.

Configuring Attributes

Describe the properties that compose an entity.

Configuring Relationships

Specify how entities relate and how change propagates between them.

