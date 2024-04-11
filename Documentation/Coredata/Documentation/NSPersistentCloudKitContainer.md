Instance Method

# record(for:)

Returns the CloudKit record for the specified managed object ID.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.1+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func record(for managedObjectID: NSManagedObjectID) -> CKRecord?

##  Parameters

`managedObjectID`

    

The ID of the managed object.

## Return Value

An instance of `CKRecord` if the managed object has an underlying CloudKit
record; otherwise, `nil`.

## See Also

### Accessing Records

`func records(for: [NSManagedObjectID]) -> [NSManagedObjectID : CKRecord]`

Returns a dictionary that contains the CloudKit records for the specified
managed object IDs.

`func recordID(for: NSManagedObjectID) -> CKRecordID?`

Returns the CloudKit record ID for the specified managed object ID.

`func recordIDs(for: [NSManagedObjectID]) -> [NSManagedObjectID : CKRecordID]`

Returns a dictionary that contains the CloudKit record IDs for the specified
managed object IDs.

Instance Method

# records(for:)

Returns a dictionary that contains the CloudKit records for the specified
managed object IDs.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.1+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func records(for managedObjectIDs: [NSManagedObjectID]) -> [NSManagedObjectID : CKRecord]

##  Parameters

`managedObjectIDs`

    

An array of managed object IDs.

## Return Value

A dictionary that uses `managedObjectIDs` as its keys, and each object’s
underlying `CKRecord` as its values. The dictionary excludes IDs that don’t
have a CloudKit record.

## See Also

### Accessing Records

`func record(for: NSManagedObjectID) -> CKRecord?`

Returns the CloudKit record for the specified managed object ID.

`func recordID(for: NSManagedObjectID) -> CKRecordID?`

Returns the CloudKit record ID for the specified managed object ID.

`func recordIDs(for: [NSManagedObjectID]) -> [NSManagedObjectID : CKRecordID]`

Returns a dictionary that contains the CloudKit record IDs for the specified
managed object IDs.

Instance Method

# recordID(for:)

Returns the CloudKit record ID for the specified managed object ID.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.1+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func recordID(for managedObjectID: NSManagedObjectID) -> CKRecordID?

##  Parameters

`managedObjectID`

    

The ID of the managed object.

## Return Value

An instance of `CKRecord.ID` if the managed object has an underlying CloudKit
record; otherwise, `nil`.

## See Also

### Accessing Records

`func record(for: NSManagedObjectID) -> CKRecord?`

Returns the CloudKit record for the specified managed object ID.

`func records(for: [NSManagedObjectID]) -> [NSManagedObjectID : CKRecord]`

Returns a dictionary that contains the CloudKit records for the specified
managed object IDs.

`func recordIDs(for: [NSManagedObjectID]) -> [NSManagedObjectID : CKRecordID]`

Returns a dictionary that contains the CloudKit record IDs for the specified
managed object IDs.

Instance Method

# recordIDs(for:)

Returns a dictionary that contains the CloudKit record IDs for the specified
managed object IDs.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.1+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func recordIDs(for managedObjectIDs: [NSManagedObjectID]) -> [NSManagedObjectID : CKRecordID]

##  Parameters

`managedObjectIDs`

    

An array of the managed object IDs.

## Return Value

A dictionary that uses `managedObjectIDs` as its keys, and the `CKRecord.ID`
of each object’s underlying CloudKit record as its values. The dictionary
excludes IDs that don’t have a CloudKit record.

## See Also

### Accessing Records

`func record(for: NSManagedObjectID) -> CKRecord?`

Returns the CloudKit record for the specified managed object ID.

`func records(for: [NSManagedObjectID]) -> [NSManagedObjectID : CKRecord]`

Returns a dictionary that contains the CloudKit records for the specified
managed object IDs.

`func recordID(for: NSManagedObjectID) -> CKRecordID?`

Returns the CloudKit record ID for the specified managed object ID.

Instance Method

# canUpdateRecord(forManagedObjectWith:)

Returns a Boolean value that indicates whether the user can modify the managed
object’s underlying CloudKit record.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    func canUpdateRecord(forManagedObjectWith objectID: NSManagedObjectID) -> Bool

##  Parameters

`objectID`

    

The ID of the managed object.

## Return Value

`true` if the user can modify the CloudKit record; otherwise, `false`.

## Discussion

This method returns `true` if `canModifyManagedObjects(in:)` returns `true`
and any of the following conditions are true:

  * `objectID` is a temporary object identifier.

  * The persistent store that contains the managed object isn’t using CloudKit.

  * The persistent store manages the user’s private database.

  * The persistent store manages the public database, and the user owns the underlying record or Core Data has yet to save the managed object to iCloud.

  * The persistent store manages the shared database, and the user has the necessary permissions to update the managed object’s underlying record. For more information, see `CKShare.ParticipantPermission`.

## See Also

### Checking Permissions

`func canDeleteRecord(forManagedObjectWith: NSManagedObjectID) -> Bool`

Returns a Boolean value that indicates whether the user can delete the managed
object’s underlying CloudKit record.

`func canModifyManagedObjects(in: NSPersistentStore) -> Bool`

Returns a Boolean value that indicates whether the user can modify the
specified persistent store.

Instance Method

# canDeleteRecord(forManagedObjectWith:)

Returns a Boolean value that indicates whether the user can delete the managed
object’s underlying CloudKit record.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    func canDeleteRecord(forManagedObjectWith objectID: NSManagedObjectID) -> Bool

##  Parameters

`objectID`

    

The ID of the managed object.

## Return Value

`true` if the user can delete the CloudKit record; otherwise, `false`.

## Discussion

This method returns `true` if `canModifyManagedObjects(in:)` returns `true`
and any of the following conditions are true:

  * `objectID` is a temporary object identifier.

  * The persistent store that contains the managed object isn’t using CloudKit.

  * The persistent store manages the user’s private database.

  * The persistent store manages the public database, and the user owns the underlying record or Core Data has yet to save the managed object to iCloud.

  * The persistent store manages the shared database, and the user has the necessary permissions to delete the managed object’s underlying record. For more information, see `CKShare.ParticipantPermission`.

## See Also

### Checking Permissions

`func canUpdateRecord(forManagedObjectWith: NSManagedObjectID) -> Bool`

Returns a Boolean value that indicates whether the user can modify the managed
object’s underlying CloudKit record.

`func canModifyManagedObjects(in: NSPersistentStore) -> Bool`

Returns a Boolean value that indicates whether the user can modify the
specified persistent store.

Instance Method

# canModifyManagedObjects(in:)

Returns a Boolean value that indicates whether the user can modify the
specified persistent store.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    func canModifyManagedObjects(in store: NSPersistentStore) -> Bool

##  Parameters

`store`

    

The persistent store.

## Return Value

`true` if the user can modify records in the persistent store’s CloudKit
database; otherwise, `false`.

## Discussion

Use this method to determine whether the user is able to write any records to
the CloudKit database. To find out if the user can modify a specific object,
use the `canUpdateRecord(forManagedObjectWith:)` and
`canDeleteRecord(forManagedObjectWith:)` methods instead.

This method always returns `true` for persistent stores that manage the user’s
private CloudKit database.

## See Also

### Checking Permissions

`func canUpdateRecord(forManagedObjectWith: NSManagedObjectID) -> Bool`

Returns a Boolean value that indicates whether the user can modify the managed
object’s underlying CloudKit record.

`func canDeleteRecord(forManagedObjectWith: NSManagedObjectID) -> Bool`

Returns a Boolean value that indicates whether the user can delete the managed
object’s underlying CloudKit record.

Article

# Accepting Share Invitations in a SwiftUI App

Adapt your app to use UIKit’s application and scene delegates so it can
process CloudKit share invitations.

## Overview

When the user accepts an invitation to participate in a CloudKit share, the
system passes that share’s metadata to your app’s scene delegate for
processing. To receive this metadata in a SwiftUI app:

  1. Add a scene delegate — an object that conforms to `UIWindowSceneDelegate` — that’s responsible for passing the accepted share metadata to your app’s persistent container.

  2. Add an application delegate — an object that conforms to `UIApplicationDelegate` — that configures new scenes to use your custom scene delegate class.

  3. Modify your app’s `App` structure to use `UIApplicationDelegateAdaptor` to initialize and manage an application delegate at runtime.

### Add a Scene Delegate to Process Share Invitations

In response to the user accepting a CloudKit share invitation, the system
routes that action, for processing, to the delegate of the app’s active scene.
SwiftUI apps don’t contain a scene delegate by default, but you can add one,
and use it to implement the `windowScene(_:userDidAcceptCloudKitShareWith:)`
method. Your implementation is responsible for passing the provided share
metadata to your app’s persistent container for processing.

To create the scene delegate, right-click your project in Xcode’s Project
navigator and select New File. Choose the Swift File template and name the
file `SceneDelegate.swift`. Open the new file in Xcode’s source editor and
define the `SceneDelegate` class as a subclass of `UIResponder` that adopts
the `UIWindowSceneDelegate` protocol. Within this class, add your
implementation of `windowScene(_:userDidAcceptCloudKitShareWith:)`, as shown
in the following example.

The example above uses a `CoreDataStack` object that manages the
initialization of the persistent container, and the private and shared
persistent stores. For a reference implementation, see the sample code project
Synchronizing a local store to the cloud.

### Add an Application Delegate to Configure New Scenes

Before an app connects a new scene, the system asks the application delegate
to provide the configuration for the new scene, including the class to use as
its own delegate. By providing this configuration, your app can use your
custom delegate implementation and correctly process accepted CloudKit share
invitations. Because SwiftUI apps don’t include an application delegate, you
need to add one to your app’s target.

Right-click your project in Xcode’s Project navigator and select New File.
Choose the Swift File template and name the file `AppDelegate.swift`. Open the
new file in Xcode’s source editor and add the following code, which configures
each new scene to use the custom `SceneDelegate` class from the previous
section.

For more information on scene configuration, see
`application(_:configurationForConnecting:options:)`.

### Modify Your App to Utilize the Application Delegate

After you add the scene and application delegates to your app’s target, use
the `UIApplicationDelegateAdaptor` property wrapper to instruct your app’s
top-level object — the structure that adopts SwiftUI’s `App` protocol — to
initialize and manage an instance of the application delegate at runtime, as
shown in the following example.

With this change in place, whenever the user accepts a CloudKit share
invitation, SwiftUI notifies the active scene’s delegate where you can process
the accepted invitation accordingly.

## See Also

### Sharing Objects

`func acceptShareInvitations(from: [CKShareMetadata], into: NSPersistentStore,
completion: (([CKShareMetadata]?, (any Error)?) -> Void)?)`

Accepts one or more invitations to participate in sharing using the specified
metadata.

`func fetchParticipants(matching: [CKUserIdentityLookupInfo], into:
NSPersistentStore, completion: ([CKShareParticipant]?, (any Error)?) -> Void)`

Fetches all participants that match the specified critieria.

`func fetchShares(in: NSPersistentStore?) -> [CKShare]`

Returns an array that contains all share records in the specified persistent
store.

`func fetchShares(matching: [NSManagedObjectID]) -> [NSManagedObjectID :
CKShare]`

Returns a dictionary that contains the share records that CloudKit associates
with specified managed object IDs.

`func persistUpdatedShare(CKShare, in: NSPersistentStore, completion:
((CKShare?, (any Error)?) -> Void)?)`

Saves the share record and schedules it for export to iCloud.

`func share([NSManagedObject], to: CKShare?, completion:
(Set<NSManagedObjectID>?, CKShare?, CKContainer?, (any Error)?) -> Void)`

Associates the specified managed objects with a new or existing share record.

Instance Method

# acceptShareInvitations(from:into:completion:)

Accepts one or more invitations to participate in sharing using the specified
metadata.

Core Data  CloudKit  iOS 15.0+  iPadOS 15.0+  macOS 12.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func acceptShareInvitations(
        from metadata: [CKShareMetadata],
        into persistentStore: NSPersistentStore,
        completion: (([CKShareMetadata]?, (any Error)?) -> Void)? = nil
    )

##  Parameters

`metadata`

    

An array of share metadata. For more information, see `CKShare.Metadata`.

`persistentStore`

    

The persistent store that provides the CloudKit container’s identifier. The
store must have the `CKDatabase.Scope.shared` database scope. For more
information, see `NSPersistentCloudKitContainerOptions`.

`completion`

    

The handler to invoke after you process the specified invitations.

## Discussion

Concurrency Note

You can call this method from synchronous code using a completion handler, as
shown on this page, or you can call it as an asynchronous method that has the
following declaration:

For information about concurrency and asynchronous code in Swift, see Calling
Objective-C APIs Asynchronously.

`completion` returns no value and takes the following parameters:

  * An array of accepted share metadata

  * An error object that contains information about a problem, or `nil` if the method successfully accepts all invitations

You typically call this method from your scene delegate’s
`windowScene(_:userDidAcceptCloudKitShareWith:)` method. For SwiftUI apps,
there are additional steps you need to complete before you can do this. For
more information, see Accepting Share Invitations in a SwiftUI App.

Note

To be able to accept the share invitations, this method requires an active
network connection. It executes a number of CloudKit operations, and imports
any shared records into the relevant persistent stores, so it may take some
time to complete.

## See Also

### Sharing Objects

Accepting Share Invitations in a SwiftUI App

Adapt your app to use UIKit’s application and scene delegates so it can
process CloudKit share invitations.

`func fetchParticipants(matching: [CKUserIdentityLookupInfo], into:
NSPersistentStore, completion: ([CKShareParticipant]?, (any Error)?) -> Void)`

Fetches all participants that match the specified critieria.

`func fetchShares(in: NSPersistentStore?) -> [CKShare]`

Returns an array that contains all share records in the specified persistent
store.

`func fetchShares(matching: [NSManagedObjectID]) -> [NSManagedObjectID :
CKShare]`

Returns a dictionary that contains the share records that CloudKit associates
with specified managed object IDs.

`func persistUpdatedShare(CKShare, in: NSPersistentStore, completion:
((CKShare?, (any Error)?) -> Void)?)`

Saves the share record and schedules it for export to iCloud.

`func share([NSManagedObject], to: CKShare?, completion:
(Set<NSManagedObjectID>?, CKShare?, CKContainer?, (any Error)?) -> Void)`

Associates the specified managed objects with a new or existing share record.

Instance Method

# fetchParticipants(matching:into:completion:)

Fetches all participants that match the specified critieria.

Core Data  CloudKit  iOS 15.0+  iPadOS 15.0+  macOS 12.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func fetchParticipants(
        matching lookupInfos: [CKUserIdentityLookupInfo],
        into persistentStore: NSPersistentStore,
        completion: @escaping ([CKShareParticipant]?, (any Error)?) -> Void
    )

##  Parameters

`lookupInfos`

    

An array of criteria that CloudKit uses to find participants. For more
information, see `CKUserIdentity.LookupInfo`.

`persistentStore`

    

The persistent store that provides the CloudKit container’s identifier. For
more information, see `NSPersistentCloudKitContainerOptions`.

`completion`

    

The handler to invoke after the method fetches participants.

## Discussion

Concurrency Note

You can call this method from synchronous code using a completion handler, as
shown on this page, or you can call it as an asynchronous method that has the
following declaration:

For information about concurrency and asynchronous code in Swift, see Calling
Objective-C APIs Asynchronously.

`completion` returns no value and takes the following parameters:

  * An array of fetched participants. For more information, see `CKShare.Participant`.

  * An error object that contains information about a problem, or `nil` if the method successfully fetches participants.

Note

To fetch participants, this method executes operations against `CKContainer`,
and requires an active network connection.

## See Also

### Sharing Objects

Accepting Share Invitations in a SwiftUI App

Adapt your app to use UIKit’s application and scene delegates so it can
process CloudKit share invitations.

`func acceptShareInvitations(from: [CKShareMetadata], into: NSPersistentStore,
completion: (([CKShareMetadata]?, (any Error)?) -> Void)?)`

Accepts one or more invitations to participate in sharing using the specified
metadata.

`func fetchShares(in: NSPersistentStore?) -> [CKShare]`

Returns an array that contains all share records in the specified persistent
store.

`func fetchShares(matching: [NSManagedObjectID]) -> [NSManagedObjectID :
CKShare]`

Returns a dictionary that contains the share records that CloudKit associates
with specified managed object IDs.

`func persistUpdatedShare(CKShare, in: NSPersistentStore, completion:
((CKShare?, (any Error)?) -> Void)?)`

Saves the share record and schedules it for export to iCloud.

`func share([NSManagedObject], to: CKShare?, completion:
(Set<NSManagedObjectID>?, CKShare?, CKContainer?, (any Error)?) -> Void)`

Associates the specified managed objects with a new or existing share record.

Instance Method

# fetchShares(in:)

Returns an array that contains all share records in the specified persistent
store.

Core Data  CloudKit  iOS 15.0+  iPadOS 15.0+  macOS 12.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func fetchShares(in persistentStore: NSPersistentStore?) throws -> [CKShare]

##  Parameters

`persistentStore`

    

The persistent store that contains the share records. Use `nil` to fetch share
records from each of the persistent container’s stores.

`error`

    

On return, an error object that contains information about a problem, or `nil`
if the method successfully fetches all share records.

## Return Value

An array of `CKShare` objects. If the fetch is successful, but Core Data
doesn’t find any share records, the method returns an empty array.

## Discussion

Use a fetched share record to manage its participants and their permissions,
or assign data directly to it. A share record is a subclass of `CKRecord`,
which means you can store any data you choose in the underlying record to meet
your specific needs. For more information, see `CKShare`.

If you modify a share record, you must save it using the
`persistUpdatedShare(_:in:completion:)` method.

Note

This method fetches known share records only. It doesn’t attempt to discover
additional record zones or share records in the persistent store’s CloudKit
database.

## See Also

### Sharing Objects

Accepting Share Invitations in a SwiftUI App

Adapt your app to use UIKit’s application and scene delegates so it can
process CloudKit share invitations.

`func acceptShareInvitations(from: [CKShareMetadata], into: NSPersistentStore,
completion: (([CKShareMetadata]?, (any Error)?) -> Void)?)`

Accepts one or more invitations to participate in sharing using the specified
metadata.

`func fetchParticipants(matching: [CKUserIdentityLookupInfo], into:
NSPersistentStore, completion: ([CKShareParticipant]?, (any Error)?) -> Void)`

Fetches all participants that match the specified critieria.

`func fetchShares(matching: [NSManagedObjectID]) -> [NSManagedObjectID :
CKShare]`

Returns a dictionary that contains the share records that CloudKit associates
with specified managed object IDs.

`func persistUpdatedShare(CKShare, in: NSPersistentStore, completion:
((CKShare?, (any Error)?) -> Void)?)`

Saves the share record and schedules it for export to iCloud.

`func share([NSManagedObject], to: CKShare?, completion:
(Set<NSManagedObjectID>?, CKShare?, CKContainer?, (any Error)?) -> Void)`

Associates the specified managed objects with a new or existing share record.

Instance Method

# fetchShares(matching:)

Returns a dictionary that contains the share records that CloudKit associates
with specified managed object IDs.

Core Data  CloudKit  iOS 15.0+  iPadOS 15.0+  macOS 12.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func fetchShares(matching objectIDs: [NSManagedObjectID]) throws -> [NSManagedObjectID : CKShare]

##  Parameters

`objectIDs`

    

An array of managed object IDs.

`error`

    

On return, an error object that contains information about a problem, or `nil`
if the method successfully fetches the share records.

## Return Value

A dictionary that uses `objectIDs` as its keys, and the associated share
records as its values.

## Discussion

If a specified managed object doesn’t belong to a shared record zone, or if
Core Data has yet to save the object to iCloud and, therefore, its record zone
is unknown, the returned dictionary doesn’t include it.

Use a fetched share record to manage its participants and their permissions,
or assign data directly to it. A share record is a subclass of `CKRecord`,
which means you can store any data you choose in the underlying record to meet
your specific needs. For more information, see `CKShare`.

If you modify a share record, you must save it using the
`persistUpdatedShare(_:in:completion:)` method.

Note

This method fetches known share records only. It doesn’t attempt to discover
additional record zones or share records in any of the persistent container’s
CloudKit databases.

## See Also

### Sharing Objects

Accepting Share Invitations in a SwiftUI App

Adapt your app to use UIKit’s application and scene delegates so it can
process CloudKit share invitations.

`func acceptShareInvitations(from: [CKShareMetadata], into: NSPersistentStore,
completion: (([CKShareMetadata]?, (any Error)?) -> Void)?)`

Accepts one or more invitations to participate in sharing using the specified
metadata.

`func fetchParticipants(matching: [CKUserIdentityLookupInfo], into:
NSPersistentStore, completion: ([CKShareParticipant]?, (any Error)?) -> Void)`

Fetches all participants that match the specified critieria.

`func fetchShares(in: NSPersistentStore?) -> [CKShare]`

Returns an array that contains all share records in the specified persistent
store.

`func persistUpdatedShare(CKShare, in: NSPersistentStore, completion:
((CKShare?, (any Error)?) -> Void)?)`

Saves the share record and schedules it for export to iCloud.

`func share([NSManagedObject], to: CKShare?, completion:
(Set<NSManagedObjectID>?, CKShare?, CKContainer?, (any Error)?) -> Void)`

Associates the specified managed objects with a new or existing share record.

Instance Method

# persistUpdatedShare(_:in:completion:)

Saves the share record and schedules it for export to iCloud.

Core Data  CloudKit  iOS 15.0+  iPadOS 15.0+  macOS 12.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func persistUpdatedShare(
        _ share: CKShare,
        in persistentStore: NSPersistentStore,
        completion: ((CKShare?, (any Error)?) -> Void)? = nil
    )

##  Parameters

`share`

    

The share record to save.

`persistentStore`

    

The persistent store that provides the database scope and the CloudKit
container’s identifier. For more information, see
`NSPersistentCloudKitContainerOptions`.

`completion`

    

The handler to invoke after the export finishes.

## Discussion

Concurrency Note

You can call this method from synchronous code using a completion handler, as
shown on this page, or you can call it as an asynchronous method that has the
following declaration:

For information about concurrency and asynchronous code in Swift, see Calling
Objective-C APIs Asynchronously.

`completion` returns no value and takes the following parameters:

  * The saved share record, or `nil` if the save fails.

  * An error object that contains information about a problem, or `nil` if the share record saves successfully.

Core Data saves the share to the persistent store before this method returns,
but doesn’t invoke the completion handler until after the export finishes.

Important

Whenever you modify a share record, save the changes using this method to keep
the record and the local store’s metadata in sync.

## See Also

### Sharing Objects

Accepting Share Invitations in a SwiftUI App

Adapt your app to use UIKit’s application and scene delegates so it can
process CloudKit share invitations.

`func acceptShareInvitations(from: [CKShareMetadata], into: NSPersistentStore,
completion: (([CKShareMetadata]?, (any Error)?) -> Void)?)`

Accepts one or more invitations to participate in sharing using the specified
metadata.

`func fetchParticipants(matching: [CKUserIdentityLookupInfo], into:
NSPersistentStore, completion: ([CKShareParticipant]?, (any Error)?) -> Void)`

Fetches all participants that match the specified critieria.

`func fetchShares(in: NSPersistentStore?) -> [CKShare]`

Returns an array that contains all share records in the specified persistent
store.

`func fetchShares(matching: [NSManagedObjectID]) -> [NSManagedObjectID :
CKShare]`

Returns a dictionary that contains the share records that CloudKit associates
with specified managed object IDs.

`func share([NSManagedObject], to: CKShare?, completion:
(Set<NSManagedObjectID>?, CKShare?, CKContainer?, (any Error)?) -> Void)`

Associates the specified managed objects with a new or existing share record.

Instance Method

# share(_:to:completion:)

Associates the specified managed objects with a new or existing share record.

Core Data  CloudKit  iOS 15.0+  iPadOS 15.0+  macOS 12.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func share(
        _ managedObjects: [NSManagedObject],
        to share: CKShare?,
        completion: @escaping (Set<NSManagedObjectID>?, CKShare?, CKContainer?, (any Error)?) -> Void
    )

##  Parameters

`managedObjects`

    

The managed objects to share.

`share`

    

A share record that identifies an existing shared record zone to associate the
managed objects with. Use `nil` to create a new shared record zone that
contains only the specified managed objects and doesn’t have any participants.

`completion`

    

The handler to invoke after Core Data shares the managed objects.

## Discussion

Concurrency Note

You can call this method from synchronous code using a completion handler, as
shown on this page, or you can call it as an asynchronous method that has the
following declaration:

For information about concurrency and asynchronous code in Swift, see Calling
Objective-C APIs Asynchronously.

`completion` returns no value and takes the following parameters:

  * The IDs of the shared objects.

  * The share record. For more information, see `CKShare`.

  * The CloudKit container of the database that stores the shared record zone. For more information, see `CKContainer`.

  * An error object that contains information about a problem, or `nil` if the managed objects share successfully.

When you invoke this method, Core Data performs a deep traversal among the
specified managed objects and adds any related object to the share.

Sharing fails if any of the following conditions apply:

  * Any objects in `managedObjects`, or those the traversal finds, belong to an existing share record.

  * Any objects in `managedObjects` belong to a persistent store that doesn’t support sharing, such as those you configure with the `CKDatabase.Scope.public` database scope.

  * The current device state doesn’t supporting shared, such as when there isn’t an active iCloud account.

You can use `completion` directly with the `init(preparationHandler:)` method
of `UICloudSharingController`, as the following example shows.

## See Also

### Sharing Objects

Accepting Share Invitations in a SwiftUI App

Adapt your app to use UIKit’s application and scene delegates so it can
process CloudKit share invitations.

`func acceptShareInvitations(from: [CKShareMetadata], into: NSPersistentStore,
completion: (([CKShareMetadata]?, (any Error)?) -> Void)?)`

Accepts one or more invitations to participate in sharing using the specified
metadata.

`func fetchParticipants(matching: [CKUserIdentityLookupInfo], into:
NSPersistentStore, completion: ([CKShareParticipant]?, (any Error)?) -> Void)`

Fetches all participants that match the specified critieria.

`func fetchShares(in: NSPersistentStore?) -> [CKShare]`

Returns an array that contains all share records in the specified persistent
store.

`func fetchShares(matching: [NSManagedObjectID]) -> [NSManagedObjectID :
CKShare]`

Returns a dictionary that contains the share records that CloudKit associates
with specified managed object IDs.

`func persistUpdatedShare(CKShare, in: NSPersistentStore, completion:
((CKShare?, (any Error)?) -> Void)?)`

Saves the share record and schedules it for export to iCloud.

Instance Method

# purgeObjectsAndRecordsInZone(with:in:completion:)

Deletes all CloudKit records in the specified record zone, along with their
corresponding managed objects.

Core Data  CloudKit  iOS 15.0+  iPadOS 15.0+  macOS 12.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func purgeObjectsAndRecordsInZone(
        with zoneID: CKRecordZoneID,
        in persistentStore: NSPersistentStore?,
        completion: ((CKRecordZoneID?, (any Error)?) -> Void)? = nil
    )

##  Parameters

`zoneID`

    

The ID of the record zone to purge.

`persistentStore`

    

The persistent store that manages the CloudKit database containing the record
zone. Use `nil` to attempt the purge in each of the container’s persistent
stores that manages a CloudKit database.

`completion`

    

The handler to invoke after Core Data purges the CloudKit records and managed
objects.

## Discussion

Concurrency Note

You can call this method from synchronous code using a completion handler, as
shown on this page, or you can call it as an asynchronous method that has the
following declaration:

For information about concurrency and asynchronous code in Swift, see Calling
Objective-C APIs Asynchronously.

`completion` returns no value and takes the following parameters:

  * The ID of the purged record zone, or `nil` if the purge fails.

  * An error object that contains information about a problem, or `nil` if Core Data successfully purges the record zone.

If `persistentStore` is `nil`, the method invokes the completion handler once
for each of the persistent container’s stores that manages a CloudKit
database.

Instance Method

# initializeCloudKitSchema(options:)

Creates the CloudKit schema for all stores in the container that manage a
CloudKit database.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.1+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func initializeCloudKitSchema(options: NSPersistentCloudKitContainerSchemaInitializationOptions = []) throws

##  Parameters

`options`

    

The options to use when creating the CloudKit schema.

## Return Value

`true` if the operations succeed; otherwise, `false`. If the operations fail,
the `error` parameter holds the underlying error.

## Discussion

To create the schema, this method creates a set of representative `CKRecord`
instances for all stores in the container that use Core Data with CloudKit,
and uploads them to CloudKit. These records have a representative value for
every field Core Data might serialize for the specified managed object model.
After successfully uploading the records, the schema is visible in the
CloudKit Dashboard and the container deletes the representative records.

Note

This method also validates the managed object model in use for a store, so if
the model isn’t valid for use with CloudKit, a validation error may return.

## See Also

### Promoting Your Schema

`struct NSPersistentCloudKitContainerSchemaInitializationOptions`

Options that control the behavior when promoting the container’s schema to
CloudKit.

Type Property

# eventChangedNotification

A notification that contains details about an event in a persistent CloudKit
container.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    class let eventChangedNotification: NSNotification.Name

## See Also

### Monitoring Container Events

`class NSPersistentCloudKitContainer.Event`

An object that represents activity in a persistent CloudKit container.

`enum NSPersistentCloudKitContainer.EventType`

The type of event in a persistent CloudKit container, either setup, import, or
export.

`class NSPersistentCloudKitContainerEventRequest`

A request to fetch setup, import, or export events in a persistent CloudKit
container.

`class NSPersistentCloudKitContainerEventResult`

The result of a request to fetch persistent CloudKit container events.

`class let eventNotificationUserInfoKey: String`

The user info dictionary key for the persistent CloudKit container event.

Type Property

# eventNotificationUserInfoKey

The user info dictionary key for the persistent CloudKit container event.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    class let eventNotificationUserInfoKey: String

## See Also

### Monitoring Container Events

`class NSPersistentCloudKitContainer.Event`

An object that represents activity in a persistent CloudKit container.

`enum NSPersistentCloudKitContainer.EventType`

The type of event in a persistent CloudKit container, either setup, import, or
export.

`class NSPersistentCloudKitContainerEventRequest`

A request to fetch setup, import, or export events in a persistent CloudKit
container.

`class NSPersistentCloudKitContainerEventResult`

The result of a request to fetch persistent CloudKit container events.

`class let eventChangedNotification: NSNotification.Name`

A notification that contains details about an event in a persistent CloudKit
container.

