Article

# Setting Up Core Data with CloudKit

Set up the classes and capabilities that sync your store to CloudKit.

## Overview

To sync your Core Data store to CloudKit, you enable the CloudKit capability
for your app. You also set up the Core Data stack with a persistent container
that is capable of managing one or more local persistent stores that are
backed by a CloudKit private database.

### Configure a New Xcode Project

When you create a new project, you specify whether you want to add support for
Core Data with CloudKit directly from the project setup interface. The
resulting project instantiates an `NSPersistentCloudKitContainer` in your
app’s delegate. Once you enable CloudKit in your project, you use this
container to manage one or more local stores that are backed with a CloudKit
database.

  1. Choose File > New > Project to create a new project.

  2. Select a project template to use as the starting point for your project, and click Next. 

  3. Select the Use Core Data and Use CloudKit checkboxes.

  4. Enter any other project details and click Next.

  5. Specify a location for your project and click Create.

Not all project templates support Core Data. If the template you want to use
doesn’t support Core Data, add Core Data to the project as described in
Setting up a Core Data stack. Then add Core Data with CloudKit as described in
Update an Existing Xcode Project.

### Enable iCloud

Core Data with CloudKit requires specific entitlements for your app to
communicate with the server. Begin by adding the iCloud capability to your
Xcode project.

  1. In Project Settings, select the Signing & Capabilities tab. 

  2. Make sure that “Automatically manage signing” is selected. 

  3. Specify your development team.

  4. Click the + Capability button, then do a search for iCloud in the Add Capability editor and select that capability.

An iCloud section appears on your app’s Signing & Capabilities page.

### Enable CloudKit and Push Notifications

Core Data with CloudKit uses the CloudKit service to access your team’s
containers. To enable CloudKit, configure the iCloud capability.

  1. In Project Settings, select the Signing & Capabilities tab. 

  2. In the iCloud section, under Services, select the CloudKit checkbox. This selection also adds push notifications that notify your app when remote content has changed.

  3. Under Containers, leave the selection as “Use default container.” 

Xcode checks that your development team supports the Push Notification and
iCloud capabilities, then registers your app’s bundle identifier and manages
provisioning profiles.

For more information about working with CloudKit containers and setting up
profiles, see Enabling CloudKit in Your App.

### Enable Remote Notifications in the Background

For CloudKit to silently notify your app when new content is available,
without presenting a user notification such as an alert, sound, or badge, you
need to enable the remote notifications background mode.

  1. In Project Settings, select the Signing & Capabilities tab. 

  2. Click the + Capability button, then do a search for Background Modes in the Add Capability editor and select that capability.

  3. Select the “Remote notifications” checkbox.

For more information about silent notifications, see Pushing background
updates to your App.

### Update an Existing Xcode Project

If you want to add Core Data with CloudKit to an app that already uses Core
Data, you need to modify both your project’s configuration and some of its
code.

First, enable iCloud, CloudKit, push notifications, and remote notifications
in the background as described in the preceeding sections. Then, replace your
persistent container with an instance of `NSPersistentCloudKitContainer`.

For example, if you created a project from the iOS Single View App template,
with the Use Core Data checkbox selected, the following code appeared in your
app’s delegate:

`NSPersistentContainer` supports only local persistent stores. To add the
ability to sync a local store to a CloudKit database, replace
`NSPersistentContainer` with the subclass `NSPersistentCloudKitContainer`.

### Manage Multiple Stores

You may wish to mirror a subset of your data using CloudKit, while keeping
other data completely local. You can add configurations to your model to
organize your data in separate stores, then choose which stores to sync to
CloudKit.

  1. Open your project’s `.xcdatamodeld` file.

  2. Choose Editor > Add Configuration.

  3. Drag each entity into a configuration.

  4. Select a configuration that you want to sync to CloudKit, then select the "Used with CloudKit" checkbox in the data model editor. Repeat for each configuration that you want to sync. 

For an app without configurations, `NSPersistentCloudKitContainer` matches the
first store description with the first CloudKit container identifier in the
entitlements.

For an app with configurations, you need to tell it which CloudKit container,
if any, to use with each store. For each of your configurations, make the
following changes to your container setup:

  1. Create an `NSPersistentStoreDescription`.

  2. Set the store description’s configuration.

  3. If this configuration should synchronize to CloudKit, set the store description’s `cloudKitContainerOptions` to an instance of `NSPersistentCloudKitContainerOptions`. Provide the container identifier of your CloudKit container in the initializer.

  4. Add the store description to the persistent container before loading the store.

The following example code creates two store descriptions: one for the “Local”
configuration, and one for the “Cloud” configuration. It then sets the cloud
store description’s `cloudKitContainerOptions` to match the store with its
CloudKit container. Finally, it updates the container’s list of persistent
store descriptions to include all local and cloud-backed store descriptions,
and loads both stores.

## See Also

### Configuring CloudKit Mirroring

Creating a Core Data Model for CloudKit

Design a CloudKit-compatible data model and initialize your CloudKit schema.

Syncing a Core Data Store with CloudKit

Synchronize objects between devices, and handle store changes in the user
interface.

Reading CloudKit Records for Core Data

Access CloudKit records created from Core Data managed objects.

Article

# Creating a Core Data Model for CloudKit

Design a CloudKit-compatible data model and initialize your CloudKit schema.

## Overview

To pass records between a Core Data store and a CloudKit database, they both
require a shared understanding of the data structure. You define this in the
Core Data model and then use that to generate a CloudKit schema.

### Create a Data Model

Use Xcode’s Core Data model editor to define your app’s entities and their
attributes, or construct your model in code. For more information, see
Creating a Core Data model and the articles under Modeling data.

CloudKit doesn’t support all the features of a Core Data model. As you design
your model, be aware of the following limitations and make sure you create a
compatible data model.

Core Data model element| CloudKit schema limitation  
---|---  
**Entities**|  Unique constraints aren’t supported.  
**Attributes**| `Undefined` and `objectID` attribute types aren’t supported.  
**Relationships**|  All relationships must be optional. Due to operation size
limitations, CloudKit may not save relationship changes atomically.All
relationships must have an inverse, in case the records synchronize out of
order.CloudKit doesn’t support the Deny deletion rule.  
**Configurations**|  Entities in a configuration must not have relationships
to entities in another configuration.  
  
For more information about how Core Data translates managed objects to
CloudKit records, see Reading CloudKit Records for Core Data.

### Initialize Your CloudKit Schema During Development

After creating your Core Data model, inform CloudKit about the types of
records it contains by initializing a development schema. This is a draft
schema that you can rewrite as often as necessary during development. You
can’t delete a record type or modify any existing attributes after you promote
a development schema to production.

Use the persistent container to initialize the development schema, which you
can do during app launch or from within one or more integration tests. To
exclude schema initialization from your production builds, use the following:

After initializing the schema, the console contains an entry similar to the
following:

    
    
    <NSCloudKitMirroringDelegate: 0x7f9699d29a90>: Successfully set up CloudKit 
        integration for store
    

While initializing the schema, Core Data creates a temporary instance of each
distinct record type in each of the container’s stores that mirror to a
CloudKit database and uploads them to the iCloud servers. After completing the
upload, the schema is visible in the CloudKit dashboard and Core Data removes
the temporary records.

For more information about configuring a CloudKit persistent container, see
Setting Up Core Data with CloudKit.

### Reset the Environment

As you change the model during development, periodically visit the CloudKit
dashboard to reset the development environment and delete the existing
development schema, before initializing a new one. For more information about
resetting the development environment, see Using CloudKit Dashboard to Manage
Databases.

### Promote the Schema to Production

When you’re happy with your data model, have a fully tested app, and are ready
to submit it to the App Store, it’s time to promote your schema from
development to production.

Important

After you promote your schema to production, the record types and their fields
are immutable and exist for all time. You can add new record types, and
additional fields to existing record types, but you can’t modify or delete
existing record types.

Initialize your schema one last time, then promote it from the CloudKit
dashboard. For more information about promoting a schema from development to
production, see Deploying the Schema.

### Update the Production Schema

Plan carefully for how your app handles forward compatibility and major
changes to the data model, because you can’t rename or delete CloudKit record
types and fields in production. Consider these strategies:

  * Migrate users to a completely new store, using `NSPersistentCloudKitContainerOptions` to associate the new store with a new container.

  * Incrementally add new fields to existing record types. If you adopt this approach, older versions of your app have access to every record a user creates, but not every field.

  * Version your entities by including a `version` attribute from the outset, and use a fetch request to select only those records that are compatible with the current version of the app. If you adopt this approach, older versions of your app won’t fetch records that a user creates with a more recent version, effectively hiding them on that device.

For example, consider a `Post` entity with a `version` attribute that stores
the version of the app that creates the record. You can use a predicate to
fetch only the records that are compatible with the current version of the
app.

Along with these choices, consider your timelines for supporting multiple
versions of your app, and for migrating users to newer app versions.

For tips on migrating records to a new schema, see Designing for CloudKit. For
more information about Core Data model migration, see Migrating your data
model automatically. For heavyweight migrations, see the Core Data Model
Versioning and Data Migration guide.

## See Also

### Configuring CloudKit Mirroring

Setting Up Core Data with CloudKit

Set up the classes and capabilities that sync your store to CloudKit.

Syncing a Core Data Store with CloudKit

Synchronize objects between devices, and handle store changes in the user
interface.

Reading CloudKit Records for Core Data

Access CloudKit records created from Core Data managed objects.

Article

# Syncing a Core Data Store with CloudKit

Synchronize objects between devices, and handle store changes in the user
interface.

## Overview

Once you set up your Xcode project (see Setting Up Core Data with CloudKit)
and initialize your development schema (see Creating a Core Data Model for
CloudKit), you’re ready to sync a Core Data store to CloudKit.

### Run Your App and Create Managed Object Instances

Run your app and begin creating `NSManagedObject` instances. The objects
automatically synchronize with the CloudKit database and propagate to other
devices logged into the same iCloud account. The tasks that send changes to
the cloud and receive remote changes in the local store happen on the system
in the background. You don’t need to add any code to your project to
synchronize records across devices.

It can be helpful to think of this process as similar to the water cycle.
Water evaporates up and rains down on a natural cadence. Similarly, changes
move from Core Data up to CloudKit and across to other devices on a natural
rhythm within the system event loop.

Generally, you can expect data to synchronize a local change within about a
minute of the change. Core Data also occasionally syncs CloudKit data in
scenarios such as when the app hasn’t synced in a long time.

### Upload Core Data Changes to CloudKit

When the user makes a change on one device, Core Data uploads the change to
CloudKit before sending it to the user’s other devices.

First, the user creates, updates, or deletes a managed object, such as adding
a post or editing a tag. When its managed object context saves changes to the
store, Core Data creates a background task for the system to convert the
`NSManagedObject` to a `CKRecord`. The system executes the task, creating the
record and uploading it to CloudKit.

For more information about background tasks, see `UIApplication`.

### Download CloudKit Changes into Core Data

After CloudKit receives a change and saves it to the CloudKit store, it
notifies the user’s other devices about the change.

First, CloudKit periodically sends push notifications to other devices on a
user’s account. Then, on each device, the system creates a background task to
download all of the changed records since the last fetch and converts them
into instances of `NSManagedObject`. Finally, Core Data saves these managed
objects into the local store.

For more information about push notifications, see User Notifications.

### Isolate the Current View from Store Changes

Consider what happens if a user deletes a record from their phone. This change
uploads to CloudKit, and later downloads to a laptop and an iPad. The iPad’s
current view may still show the record if the UI hasn’t updated with the
changes yet. The user taps on the now-deleted record, which is no longer
available in the store. This may lead to inconsistent representation of the
record, such as missing data, in your UI.

For this reason, you need to isolate the current view from changes to the
store by ensuring that the records the view expects continue to exist. Using
query generations, you pin the persistent container’s `viewContext` to a
specific generation of store data. This allows the context to fulfill faults —
placeholder objects whose values haven’t yet been fetched — that existed at
the time the view loaded, even if the store changes underneath.

Pin a context to a query generation before its first read from the store.

Any time you save, merge, or reset the context, it automatically updates its
pin to the current query generation.

For more information about faults, see Faulting and Uniquing.

For more information about query generations, see Accessing data when the
store changes.

### Integrate Store Changes Relevant to the Current View

Your app receives remote change notifications when the local store updates
from CloudKit. However, it’s unnecessary to update your UI in response to
every notification, because some changes may not be relevant to the current
view.

Analyze the persistent history to determine whether the changes are relevant
to the current view before consuming them in the user interface. Inspect the
details of each transaction, such as the entity name, its updated properties,
and the type of change, to decide whether to act.

For more information about persistent history tracking, see Consuming relevant
store changes.

### Debug Errors in Core Data with CloudKit

Most errors, like those that result from a network failure or a user not being
signed in, are transient and don’t require action. You can choose the level of
detail that Core Data with CloudKit logs to the system log.

Choose Product > Scheme > Edit Scheme. Select an action such as Run, and
select the Arguments tab. Pass the `com.apple.CoreData.CloudKitDebug` user
default setting with a debug level value as an argument to the application.

Higher argument values produce more information; start at `1` and increase if
you need more detail. For more information about handling errors, see
Troubleshooting Core Data.

If you observe persistent errors that don’t automatically recover, file a bug.
For more information about bug reporting, see Submitting Bugs and Feedback.

### Inspect Logs to See What Happened

If Core Data with CloudKit doesn’t appear to be syncing, confirm that you’re
testing on two unlocked devices logged into the same iCloud account, with good
wireless internet connections.

Push notifications may get dropped or deferred, so don’t rely on them for
testing. Watch system logs to observe the status and result of expected
activity. Run the `log stream` command from the terminal, filtering by process
and container ID. If the logs don’t include the operation, your push may have
been dropped. Check the originating device for export activity.

Filter CloudKit logs to see operations on the `cloudd` process for your
container.

Filter Core Data logs to see information about the mirroring delegate’s setup,
exports, and imports for your process.

Or monitor both CloudKit and Core Data logs at the same time.

For more information about logging, see Viewing Log Messages.

## See Also

### Configuring CloudKit Mirroring

Setting Up Core Data with CloudKit

Set up the classes and capabilities that sync your store to CloudKit.

Creating a Core Data Model for CloudKit

Design a CloudKit-compatible data model and initialize your CloudKit schema.

Reading CloudKit Records for Core Data

Access CloudKit records created from Core Data managed objects.

Article

# Reading CloudKit Records for Core Data

Access CloudKit records created from Core Data managed objects.

## Overview

Although your Core Data app interacts primarily with managed objects, you can
access a managed object’s `CKRecord` directly. This is useful if you’re
leveraging CloudKit to add features like sharing. You can also use CloudKit JS
to access CloudKit records from your web app.

To prevent collision with existing CloudKit record types and reserved names,
CloudKit prefixes the `CKRecord` types and fields it creates for your Core
Data entities with `CD_`.

To work with records directly, you need to understand the mappings between
entities and record types, attributes and fields, and the ways a record stores
relationships.

Note

Core Data doesn’t use CloudKit’s native support for relationships,
`CKRecord.Reference`, because this field limits the number of references to
750, and cannot represent many-to-many relationships. Core Data stores the
relationship in CloudKit according to its cardinality (one-to-one, one-to-
many, or many-to-many), as described in this article.

### Read Entities from Record Types

CloudKit doesn’t typically support inheritance, so it provides only a single
system field, `recordType`, to hold type information. Core Data stores the
name of the _root entity_ from the inheritance hierarchy in `recordType`.

When you initialize a schema, Core Data adds a custom field to the record
type, `CD_entityName`, to store the name of the _current entity_.

For example, an entity named `Post` generates the following structure (before
adding its attributes), with its `CD_entityName` set to `Post`, and its
`recordType` set to `CD_Post`.

Consider a second entity, `ImagePost`, that inherits from Post.

`ImagePost` generates the following structure (before adding its attributes),
with its `CD_entityName` set to `ImagePost`, and its `recordType` set to
`CD_Post`.

Query against `recordType` when searching against an entity’s inheritance
hierarchy. Query against `CD_entityName` when searching for instances of a
specific type.

For more information about CloudKit queries, see `CKQuery`.

### Read Attributes from Fields

When you initialize a schema, Core Data creates fields for each of an entity’s
attributes, mapping the attribute name to a field with a key in the form
`CD_[attribute.name]`. The field’s type may vary between Core Data and
CloudKit.

Core Data attribute type| `NSManagedObject` attribute type| `CKRecord`
attribute type  
---|---|---  
`Integer 16`| `NSNumber`| `NSNumber`  
`Integer 32`| `NSNumber`| `NSNumber`  
`Integer 64`| `NSNumber`| `NSNumber`  
`Double`| `NSNumber`| `NSNumber`  
`Float`| `NSNumber`| `NSNumber`  
`Boolean`| `NSNumber`| `NSNumber`  
`Date`| `NSDate`| `NSDate`  
`Decimal`| `NSDecimalNumber`| `NSNumber`  
`UUID`| `NSUUID`| `NSString`  
`URI`| `NSURL`| `NSString`  
`String`| `NSString`| `NSString` or `CKAsset`  
`Binary Data`| `NSData`| `NSData` or `CKAsset`  
`Transformable`| `NSData`| `NSData` or `CKAsset`  
`Undefined `| —| not supported  
`Object ID`| —| not supported  
  
All variable length attribute types—String, Binary Data, and
Transformable—generate an additional field with a key in the form
`CD_[attribute.name]_ckAsset`. If a field’s value grows too large to store
within the record size limit of 1MB, Core Data automatically converts the
value to an external asset. Core Data transitions between the original field
and its asset counterpart transparently during serialization. When inspecting
a CloudKit record directly, check the length of the original field’s value; if
it is zero, look in the asset field.

For example, an entity named `Post` with String `content` and `title`
attributes would generate the following fully materialized record, with pairs
of fields for `CD_content and` `CD_content_ckAsset`, and for `CD_title` and
`CD_title_ckAsset`.

### Read One-to-One Relationships from Fields

One-to-one relationships store foreign keys in both related records, mapping
the relationship name to a field with a key in the form
`CD_[relationship.name]`. This field stores the foreign key of the related
object in the form `CKRecord.recordID.recordName`.

For example, consider a one-to-one relationship between an `ImageData` entity
and an `Attachment` entity. In Core Data, the `Attachment` has an `imageData`
relationship, and the `ImageData` has an `attachment` relationship.

This one-to-one relationship between `ImageData` and `Attachment` would
generate the following CloudKit records.

The `CD_imageData` field on the `CD_Attachment` contains the foreign key of
the image, and the `CD_attachment` field on the `CD_ImageData` contains the
foreign key of the attachment.

### Read One-to-Many Relationships from Fields

One-to-many relationships store a foreign key on each record on the many side
of the relationship, mapping the relationship name to a field with a key in
the form `CD_[relationship name]`. This field stores the foreign key of the
related object in the form `CKRecord.recordID.recordName`.

For example, a one-to-many relationship between a single `Post` and multiple
`Attachment` instances would generate multiple `CD_Attachment` records. Each
record contains the foreign key of the `Post` it belongs to in their `CD_post`
field.

Generated `Post` records don’t contain a reference to their attachments.

### Read Many-to-Many Relationships from CDMR Records

Many-to-many relationships model the join table using a custom Core Data
Mirrored Relationship (CDMR) record type.

CloudKit doesn’t support the notion of a join, and it’s inefficient to encode
arrays on both records and keep them in sync. Instead, Core Data constructs a
CDMR record to accurately and succintly capture all of the criteria of the
join.

CDMR records have the following fields.

CDMR Field| Description  
---|---  
`CD_entityNames`| An alphabetically sorted, semicolon-separated list of the
entities in the relationship, for example, `“Post:Tag”`. The ordering of this
field determines the ordering for all other fields.  
`CD_recordNames`| The record names of the two related objects, for example,
`“CD_Post_F587C290-BC2F-441B-98FC-1357BA89C411:CD_Tag_215FA1E0-6A16-4A2B-BFA2-C13202BE6D50”`,
sorted according to the CD_entityNames order.  
`CD_relationships`| The relationship names, for example, `“tags:posts”`,
sorted according to the CD_entityNames order.  
  
For example, consider a many-to-many relationship between `Tag` and `Post`
entities.

The individual `Tag` and `Post` records don’t contain fields for the
relationship.

The relationship between any two `Tag` and `Post` records exists in a third
CDMR record. The CDMR record describes the entity type, record name, and Core
Data relationship between the `Tag` and `Post`.

The structure of a CDMR record is carefully designed to occupy the minimum
necessary footprint, and to require the least effort to decode and work with,
making it usable outside the Core Data framework.

### Access CloudKit Objects

You can access a managed object’s `CKRecord` directly through its associated
context using `record(for:)` for a single record, or `records(for:)` for
multiple records. To retrieve the record ID only, use `recordID(for:)`, or
`recordIDs(for:)`.

Alternatively, use the class functions `record(for:)`, `records(for:)`,
`recordID(for:)`, and `recordIDs(for:)` on `NSPersistentCloudKitContainer`.

## See Also

### Configuring CloudKit Mirroring

Setting Up Core Data with CloudKit

Set up the classes and capabilities that sync your store to CloudKit.

Creating a Core Data Model for CloudKit

Design a CloudKit-compatible data model and initialize your CloudKit schema.

Syncing a Core Data Store with CloudKit

Synchronize objects between devices, and handle store changes in the user
interface.

