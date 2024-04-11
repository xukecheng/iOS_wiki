Initializer

# init(name:)

Creates a container with the specified name.

iOS 10.0+  iPadOS 10.0+  macOS 10.12+  Mac Catalyst 13.1+  tvOS 10.0+  watchOS
3.0+  visionOS 1.0+

    
    
    convenience init(name: String)

##  Parameters

`name`

    

The name of the `NSPersistentContainer` object.

## Return Value

A persistent container initialized with the given name.

## Discussion

By default, the provided name value is used to name the persistent store and
is used to look up the name of the `NSManagedObjectModel` object to be used
with the `NSPersistentContainer` object.

## See Also

### Creating a Container

`init(name: String, managedObjectModel: NSManagedObjectModel)`

Create a container with the specified name and managed object model.

Initializer

# init(name:managedObjectModel:)

Create a container with the specified name and managed object model.

iOS 10.0+  iPadOS 10.0+  macOS 10.12+  Mac Catalyst 13.1+  tvOS 10.0+  watchOS
3.0+  visionOS 1.0+

    
    
    init(
        name: String,
        managedObjectModel model: NSManagedObjectModel
    )

##  Parameters

`name`

    

The name used by the persistent container.

`model`

    

The managed object model to be used by the persistent container.

## Return Value

A persistent container initialized with the given name and model.

## Discussion

By default, the provided name value of the container is used as the name of
the persisent store associated with the container. Passing in the
`NSManagedObjectModel` object overrides the lookup of the model by the
provided name value.

## See Also

### Creating a Container

`init(name: String)`

Creates a container with the specified name.

Instance Property

# managedObjectModel

The container’s managed object model.

iOS 10.0+  iPadOS 10.0+  macOS 10.12+  Mac Catalyst 13.1+  tvOS 10.0+  watchOS
3.0+  visionOS 1.0+

    
    
    var managedObjectModel: NSManagedObjectModel { get }

## Discussion

This property contains a reference to the `NSManagedObjectModel` object
associated with this persistent container.

## See Also

### Getting the Container’s Configuration

`var name: String`

The container’s name.

`var persistentStoreCoordinator: NSPersistentStoreCoordinator`

The container’s persistent store coordinator.

Instance Property

# name

The container’s name.

iOS 10.0+  iPadOS 10.0+  macOS 10.12+  Mac Catalyst 13.1+  tvOS 10.0+  watchOS
3.0+  visionOS 1.0+

    
    
    var name: String { get }

## Discussion

This property is passed in as part of the initialization of the persistent
container. This name is used to locate the `NSManagedObjectModel` (if the
`NSManagedObjectModel` object is not passed in as part of the initialization)
and is used to name the persistent store.

## See Also

### Getting the Container’s Configuration

`var managedObjectModel: NSManagedObjectModel`

The container’s managed object model.

`var persistentStoreCoordinator: NSPersistentStoreCoordinator`

The container’s persistent store coordinator.

Instance Property

# persistentStoreCoordinator

The container’s persistent store coordinator.

iOS 10.0+  iPadOS 10.0+  macOS 10.12+  Mac Catalyst 13.1+  tvOS 10.0+  watchOS
3.0+  visionOS 1.0+

    
    
    var persistentStoreCoordinator: NSPersistentStoreCoordinator { get }

## Discussion

When the persistent container is initialized, it creates a persistent store
coordinator as part of that initialization. That persistent store coordinator
is referenced in this property.

## See Also

### Getting the Container’s Configuration

`var managedObjectModel: NSManagedObjectModel`

The container’s managed object model.

`var name: String`

The container’s name.

Type Property

# defaultDirectoryURL

The location of the directory that contains the persistent stores.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    class var defaultDirectoryURL: URL { get }

## See Also

### Accessing the Default Directory

`class func defaultDirectoryURL() -> URL`

Returns the location of the directory that contains the persistent stores.

Type Method

# defaultDirectoryURL()

Returns the location of the directory that contains the persistent stores.

iOS 10.0+  iPadOS 10.0+  macOS 10.12+  Mac Catalyst 13.1+  tvOS 10.0+  watchOS
3.0+  visionOS 1.0+

    
    
    class func defaultDirectoryURL() -> URL

## Return Value

An `NSURL` that references the directory in which the persistent store(s) will
be located or are currently located.

## Discussion

This method returns a platform-dependent `NSURL` at which the persistent
store(s) will be located or are currently located. This method can be
overridden in a subclass of `NSPersistentContainer`.

## See Also

### Accessing the Default Directory

`class var defaultDirectoryURL: URL`

The location of the directory that contains the persistent stores.

Instance Property

# persistentStoreDescriptions

The descriptions of the container’s persistent stores.

iOS 10.0+  iPadOS 10.0+  macOS 10.12+  Mac Catalyst 13.1+  tvOS 10.0+  watchOS
3.0+  visionOS 1.0+

    
    
    var persistentStoreDescriptions: [NSPersistentStoreDescription] { get set }

## Discussion

If you want to override the type (or types) of persistent store(s) used by the
persistent container, you can set this property with an array of
`NSPersistentStoreDescription` objects.

If you will be configuring custom persistent store descriptions, you must set
this property before calling `loadPersistentStores(completionHandler:)`.

## See Also

### Managing Persistent Stores

`func loadPersistentStores(completionHandler: (NSPersistentStoreDescription,
(any Error)?) -> Void)`

Loads the persistent stores.

Instance Method

# loadPersistentStores(completionHandler:)

Loads the persistent stores.

iOS 10.0+  iPadOS 10.0+  macOS 10.12+  Mac Catalyst 13.1+  tvOS 10.0+  watchOS
3.0+  visionOS 1.0+

    
    
    func loadPersistentStores(completionHandler block: @escaping (NSPersistentStoreDescription, (any Error)?) -> Void)

##  Parameters

`block`

    

Once the loading of the persistent stores has completed, this block will be
executed on the calling thread.

## Discussion

Once the persistent container has been initialized, you need to execute
`loadPersistentStores(completionHandler:)` to instruct the container to load
the persistent stores and complete the creation of the Core Data stack.

Once the completion handler has fired, the stack is fully initialized and is
ready for use. The completion handler will be called once for each persistent
store that is created.

If there is an error in the loading of the persistent stores, the `NSError`
value will be populated.

## See Also

### Managing Persistent Stores

`var persistentStoreDescriptions: [NSPersistentStoreDescription]`

The descriptions of the container’s persistent stores.

Instance Method

# newBackgroundContext()

Returns a new managed object context that executes on a private queue.

iOS 10.0+  iPadOS 10.0+  macOS 10.12+  Mac Catalyst 13.1+  tvOS 10.0+  watchOS
3.0+  visionOS 1.0+

    
    
    func newBackgroundContext() -> NSManagedObjectContext

## Return Value

A newly created private managed object context.

## Discussion

Invoking this method causes the persistent container to create and return a
new `NSManagedObjectContext` with the `concurrencyType` set to
`NSManagedObjectContextConcurrencyType.privateQueueConcurrencyType`. This new
context will be associated with the `NSPersistentStoreCoordinator` directly
and is set to consume `NSManagedObjectContextDidSave` broadcasts
automatically.

## See Also

### Acquiring Contexts

`var viewContext: NSManagedObjectContext`

The main queue’s managed object context.

Instance Property

# viewContext

The main queue’s managed object context.

iOS 10.0+  iPadOS 10.0+  macOS 10.12+  Mac Catalyst 13.1+  tvOS 10.0+  watchOS
3.0+  visionOS 1.0+

    
    
    var viewContext: NSManagedObjectContext { get }

## Discussion

This property contains a reference to the `NSManagedObjectContext` that is
created and owned by the persistent container which is associated with the
main queue of the application. This context is created automatically as part
of the initialization of the persistent container.

This context is associated directly with the `NSPersistentStoreCoordinator`
and is non-generational by default.

## See Also

### Acquiring Contexts

`func newBackgroundContext() -> NSManagedObjectContext`

Returns a new managed object context that executes on a private queue.

Instance Method

# performBackgroundTask(_:)

Executes a closure on a private queue using an ephemeral managed object
context.

iOS 10.0+  iPadOS 10.0+  macOS 10.12+  Mac Catalyst 13.1+  tvOS 10.0+  watchOS
3.0+  visionOS 1.0+

    
    
    func performBackgroundTask(_ block: @escaping (NSManagedObjectContext) -> Void)

##  Parameters

`block`

    

A block that is executed by the persistent container against a newly created
private context. The private context is passed into the block as part of the
execution of the block.

## Discussion

Each time this method is invoked, the persistent container creates a new
`NSManagedObjectContext` with the `concurrencyType` set to
`NSManagedObjectContextConcurrencyType.privateQueueConcurrencyType`. The
persistent container then executes the passed in block against that newly
created context on the context’s private queue.

## See Also

### Performing Background Tasks

`func performBackgroundTask<T>((NSManagedObjectContext) -> T) -> T`

Generic Instance Method

# performBackgroundTask(_:)

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    func performBackgroundTask<T>(_ block: @escaping (NSManagedObjectContext) throws -> T) async rethrows -> T

## See Also

### Performing Background Tasks

`func performBackgroundTask((NSManagedObjectContext) -> Void)`

Executes a closure on a private queue using an ephemeral managed object
context.

