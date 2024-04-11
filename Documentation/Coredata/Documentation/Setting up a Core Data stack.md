Article

# Setting up a Core Data stack manually

Create the individual components that Core Data requires manually, to support
earlier versions of Apple operating systems.

## Overview

If your app targets iOS 10+, macOS 10.12+, tvOS 10+, watchOS 3+, or visionOS
1+, you can use `NSPersistentContainer` to simplify creation and management of
the Core Data stack. Otherwise, you need to manually create an
`NSManagedObjectModel`, `NSPersistentStoreCoordinator`, and at least one
`NSManagedObjectContext`.

### Create a managed object model

To instantiate an `NSManagedObjectModel`, pass in a URL that points to the
compiled version of the `.xcdatamodeld` file. This `.momd` file is typically
part of your app bundle.

### Create a persistent store coordinator

Next, pass the managed object model to the `NSPersistentStoreCoordinator`
initializer to create a store coordinator with that model.

#### Add a persistent store to the coordinator

If you want Core Data to persist your data model to disk, tell the store
coordinator where the file exists and what format to use.

Important

If you don’t use `NSPersistentContainer` to set up your Core Data stack, you
also need to manually set the options to enable lightweight data migrations.
For more information, see Migrating your data model automatically.

There are advantages and disadvantages to each of the store types. Refer to
the `NSPersistentStoreCoordinator` documentation for details on each store
type.

### Create a managed object context

Create an `NSManagedObjectContext`, and set its store coordinator property.

Your app uses this context to interact with Core Data. Pass a reference to
this context to your user interface. For additional information, see Inject
the managed object context.

