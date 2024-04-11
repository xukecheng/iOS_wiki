Initializer

# init(entity:dictionaryHandler:)

Creates a batch-insertion request for a managed entity, and specifies a
closure that provides data dictionaries for insertion.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    convenience init(
        entity: NSEntityDescription,
        dictionaryHandler handler: @escaping (NSMutableDictionary) -> Bool
    )

##  Parameters

`entity`

    

A managed entity to insert data into.

`handler`

    

A closure that provides a dictionary that represents an object to insert. The
dictionary contains an attribute name key and a value.

## Return Value

A batch-insertion request.

## Discussion

Core Data repeatedly calls the provided closure until it returns `true`, then
finishes the request and saves the data.

## See Also

### Creating a Request

`init(entity: NSEntityDescription, managedObjectHandler: (NSManagedObject) ->
Bool)`

Creates a batch-insertion request for a managed entity, and specifies a
closure that inserts data into the entity.

`init(entityName: String, dictionaryHandler: (NSMutableDictionary) -> Bool)`

Creates a batch-insertion request for a named managed entity, and specifies a
closure that provides data dictionaries for insertion.

`init(entityName: String, managedObjectHandler: (NSManagedObject) -> Bool)`

Creates a batch-insertion request for a named managed entity, and specifies a
closure that inserts data into the entity.

`init(entity: NSEntityDescription, objects: [[String : Any]])`

Creates a batch-insertion request for a managed entity, and provides an array
of data dictionaries for insertion.

`init(entityName: String, objects: [[String : Any]])`

Creates a batch-insertion request for a named managed entity, and provides an
array of data dictionaries for insertion.

`init()`

Creates a Core Data batch-insertion request.

Deprecated

Initializer

# init(entity:managedObjectHandler:)

Creates a batch-insertion request for a managed entity, and specifies a
closure that inserts data into the entity.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    convenience init(
        entity: NSEntityDescription,
        managedObjectHandler handler: @escaping (NSManagedObject) -> Bool
    )

##  Parameters

`entity`

    

A managed entity to insert data into.

`handler`

    

A closure that inserts data into the managed entity.

## Return Value

A batch-insertion request.

## Discussion

Core Data repeatedly calls the provided closure until it returns `true`, then
finishes the request and saves the data.

## See Also

### Creating a Request

`init(entity: NSEntityDescription, dictionaryHandler: (NSMutableDictionary) ->
Bool)`

Creates a batch-insertion request for a managed entity, and specifies a
closure that provides data dictionaries for insertion.

`init(entityName: String, dictionaryHandler: (NSMutableDictionary) -> Bool)`

Creates a batch-insertion request for a named managed entity, and specifies a
closure that provides data dictionaries for insertion.

`init(entityName: String, managedObjectHandler: (NSManagedObject) -> Bool)`

Creates a batch-insertion request for a named managed entity, and specifies a
closure that inserts data into the entity.

`init(entity: NSEntityDescription, objects: [[String : Any]])`

Creates a batch-insertion request for a managed entity, and provides an array
of data dictionaries for insertion.

`init(entityName: String, objects: [[String : Any]])`

Creates a batch-insertion request for a named managed entity, and provides an
array of data dictionaries for insertion.

`init()`

Creates a Core Data batch-insertion request.

Deprecated

Initializer

# init(entityName:dictionaryHandler:)

Creates a batch-insertion request for a named managed entity, and specifies a
closure that provides data dictionaries for insertion.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    convenience init(
        entityName: String,
        dictionaryHandler handler: @escaping (NSMutableDictionary) -> Bool
    )

##  Parameters

`entityName`

    

The name of the managed entity to insert data into.

`handler`

    

A closure that provides a dictionary that represents an object to insert. The
dictionary contains an attribute name key and a value.

## Return Value

A batch-insertion request.

## Discussion

Core Data repeatedly calls the provided closure until it returns `true`, then
finishes the request and saves the data.

## See Also

### Creating a Request

`init(entity: NSEntityDescription, dictionaryHandler: (NSMutableDictionary) ->
Bool)`

Creates a batch-insertion request for a managed entity, and specifies a
closure that provides data dictionaries for insertion.

`init(entity: NSEntityDescription, managedObjectHandler: (NSManagedObject) ->
Bool)`

Creates a batch-insertion request for a managed entity, and specifies a
closure that inserts data into the entity.

`init(entityName: String, managedObjectHandler: (NSManagedObject) -> Bool)`

Creates a batch-insertion request for a named managed entity, and specifies a
closure that inserts data into the entity.

`init(entity: NSEntityDescription, objects: [[String : Any]])`

Creates a batch-insertion request for a managed entity, and provides an array
of data dictionaries for insertion.

`init(entityName: String, objects: [[String : Any]])`

Creates a batch-insertion request for a named managed entity, and provides an
array of data dictionaries for insertion.

`init()`

Creates a Core Data batch-insertion request.

Deprecated

Initializer

# init(entityName:managedObjectHandler:)

Creates a batch-insertion request for a named managed entity, and specifies a
closure that inserts data into the entity.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    convenience init(
        entityName: String,
        managedObjectHandler handler: @escaping (NSManagedObject) -> Bool
    )

##  Parameters

`entityName`

    

The name of the managed entity that defines the object to create.

`handler`

    

A closure that inserts data into the managed entity.

## Return Value

A batch-insertion request.

## Discussion

Core Data repeatedly calls the provided closure until it returns `true`, then
finishes the request and saves the data.

## See Also

### Creating a Request

`init(entity: NSEntityDescription, dictionaryHandler: (NSMutableDictionary) ->
Bool)`

Creates a batch-insertion request for a managed entity, and specifies a
closure that provides data dictionaries for insertion.

`init(entity: NSEntityDescription, managedObjectHandler: (NSManagedObject) ->
Bool)`

Creates a batch-insertion request for a managed entity, and specifies a
closure that inserts data into the entity.

`init(entityName: String, dictionaryHandler: (NSMutableDictionary) -> Bool)`

Creates a batch-insertion request for a named managed entity, and specifies a
closure that provides data dictionaries for insertion.

`init(entity: NSEntityDescription, objects: [[String : Any]])`

Creates a batch-insertion request for a managed entity, and provides an array
of data dictionaries for insertion.

`init(entityName: String, objects: [[String : Any]])`

Creates a batch-insertion request for a named managed entity, and provides an
array of data dictionaries for insertion.

`init()`

Creates a Core Data batch-insertion request.

Deprecated

Initializer

# init(entity:objects:)

Creates a batch-insertion request for a managed entity, and provides an array
of data dictionaries for insertion.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.1+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init(
        entity: NSEntityDescription,
        objects dictionaries: [[String : Any]]
    )

##  Parameters

`entity`

    

The managed entity to insert data into.

`dictionaries`

    

An array of dictionaries that represents objects to insert. Each dictionary
contains an attribute name key and a value.

## Return Value

A batch-insertion request.

## See Also

### Creating a Request

`init(entity: NSEntityDescription, dictionaryHandler: (NSMutableDictionary) ->
Bool)`

Creates a batch-insertion request for a managed entity, and specifies a
closure that provides data dictionaries for insertion.

`init(entity: NSEntityDescription, managedObjectHandler: (NSManagedObject) ->
Bool)`

Creates a batch-insertion request for a managed entity, and specifies a
closure that inserts data into the entity.

`init(entityName: String, dictionaryHandler: (NSMutableDictionary) -> Bool)`

Creates a batch-insertion request for a named managed entity, and specifies a
closure that provides data dictionaries for insertion.

`init(entityName: String, managedObjectHandler: (NSManagedObject) -> Bool)`

Creates a batch-insertion request for a named managed entity, and specifies a
closure that inserts data into the entity.

`init(entityName: String, objects: [[String : Any]])`

Creates a batch-insertion request for a named managed entity, and provides an
array of data dictionaries for insertion.

`init()`

Creates a Core Data batch-insertion request.

Deprecated

Initializer

# init(entityName:objects:)

Creates a batch-insertion request for a named managed entity, and provides an
array of data dictionaries for insertion.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.1+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init(
        entityName: String,
        objects dictionaries: [[String : Any]]
    )

##  Parameters

`entityName`

    

The name of the managed entity to insert data into.

`dictionaries`

    

An array of dictionaries that represents objects to insert. Each dictionary
contains an attribute name key and a value.

## Return Value

A batch-insertion request.

## See Also

### Creating a Request

`init(entity: NSEntityDescription, dictionaryHandler: (NSMutableDictionary) ->
Bool)`

Creates a batch-insertion request for a managed entity, and specifies a
closure that provides data dictionaries for insertion.

`init(entity: NSEntityDescription, managedObjectHandler: (NSManagedObject) ->
Bool)`

Creates a batch-insertion request for a managed entity, and specifies a
closure that inserts data into the entity.

`init(entityName: String, dictionaryHandler: (NSMutableDictionary) -> Bool)`

Creates a batch-insertion request for a named managed entity, and specifies a
closure that provides data dictionaries for insertion.

`init(entityName: String, managedObjectHandler: (NSManagedObject) -> Bool)`

Creates a batch-insertion request for a named managed entity, and specifies a
closure that inserts data into the entity.

`init(entity: NSEntityDescription, objects: [[String : Any]])`

Creates a batch-insertion request for a managed entity, and provides an array
of data dictionaries for insertion.

`init()`

Creates a Core Data batch-insertion request.

Deprecated

Initializer

# init()

Creates a Core Data batch-insertion request.

iOS 13.0–14.0  Deprecated  iPadOS 13.0–14.0  Deprecated  macOS 10.15–11.0
Deprecated  Mac Catalyst 13.1–14.0  Deprecated  tvOS 13.0–14.0  Deprecated
watchOS 6.0–7.0  Deprecated  visionOS 1.0–1.0  Deprecated

    
    
    convenience init()

## See Also

### Creating a Request

`init(entity: NSEntityDescription, dictionaryHandler: (NSMutableDictionary) ->
Bool)`

Creates a batch-insertion request for a managed entity, and specifies a
closure that provides data dictionaries for insertion.

`init(entity: NSEntityDescription, managedObjectHandler: (NSManagedObject) ->
Bool)`

Creates a batch-insertion request for a managed entity, and specifies a
closure that inserts data into the entity.

`init(entityName: String, dictionaryHandler: (NSMutableDictionary) -> Bool)`

Creates a batch-insertion request for a named managed entity, and specifies a
closure that provides data dictionaries for insertion.

`init(entityName: String, managedObjectHandler: (NSManagedObject) -> Bool)`

Creates a batch-insertion request for a named managed entity, and specifies a
closure that inserts data into the entity.

`init(entity: NSEntityDescription, objects: [[String : Any]])`

Creates a batch-insertion request for a managed entity, and provides an array
of data dictionaries for insertion.

`init(entityName: String, objects: [[String : Any]])`

Creates a batch-insertion request for a named managed entity, and provides an
array of data dictionaries for insertion.

Instance Property

# dictionaryHandler

A closure that provides a dictionary for your app to insert data into.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    var dictionaryHandler: ((NSMutableDictionary) -> Bool)? { get set }

## See Also

### Configuring a Request

`var entity: NSEntityDescription?`

The managed entity to insert data into.

`var entityName: String`

The name of the managed entity to insert data into.

`var managedObjectHandler: ((NSManagedObject) -> Bool)?`

A closure that provides a managed object for your app to insert data into.

`var objectsToInsert: [[String : Any]]?`

An array of dictionaries that represents the objects to insert with the keys
as attribute names and their assigned values.

`var resultType: NSBatchInsertRequestResultType`

The type of result that Core Data returns from this request.

Instance Property

# entity

The managed entity to insert data into.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.1+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var entity: NSEntityDescription? { get }

## See Also

### Configuring a Request

`var dictionaryHandler: ((NSMutableDictionary) -> Bool)?`

A closure that provides a dictionary for your app to insert data into.

`var entityName: String`

The name of the managed entity to insert data into.

`var managedObjectHandler: ((NSManagedObject) -> Bool)?`

A closure that provides a managed object for your app to insert data into.

`var objectsToInsert: [[String : Any]]?`

An array of dictionaries that represents the objects to insert with the keys
as attribute names and their assigned values.

`var resultType: NSBatchInsertRequestResultType`

The type of result that Core Data returns from this request.

Instance Property

# entityName

The name of the managed entity to insert data into.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.1+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var entityName: String { get }

## See Also

### Configuring a Request

`var dictionaryHandler: ((NSMutableDictionary) -> Bool)?`

A closure that provides a dictionary for your app to insert data into.

`var entity: NSEntityDescription?`

The managed entity to insert data into.

`var managedObjectHandler: ((NSManagedObject) -> Bool)?`

A closure that provides a managed object for your app to insert data into.

`var objectsToInsert: [[String : Any]]?`

An array of dictionaries that represents the objects to insert with the keys
as attribute names and their assigned values.

`var resultType: NSBatchInsertRequestResultType`

The type of result that Core Data returns from this request.

Instance Property

# managedObjectHandler

A closure that provides a managed object for your app to insert data into.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    var managedObjectHandler: ((NSManagedObject) -> Bool)? { get set }

## See Also

### Configuring a Request

`var dictionaryHandler: ((NSMutableDictionary) -> Bool)?`

A closure that provides a dictionary for your app to insert data into.

`var entity: NSEntityDescription?`

The managed entity to insert data into.

`var entityName: String`

The name of the managed entity to insert data into.

`var objectsToInsert: [[String : Any]]?`

An array of dictionaries that represents the objects to insert with the keys
as attribute names and their assigned values.

`var resultType: NSBatchInsertRequestResultType`

The type of result that Core Data returns from this request.

Instance Property

# objectsToInsert

An array of dictionaries that represents the objects to insert with the keys
as attribute names and their assigned values.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.1+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var objectsToInsert: [[String : Any]]? { get set }

## See Also

### Configuring a Request

`var dictionaryHandler: ((NSMutableDictionary) -> Bool)?`

A closure that provides a dictionary for your app to insert data into.

`var entity: NSEntityDescription?`

The managed entity to insert data into.

`var entityName: String`

The name of the managed entity to insert data into.

`var managedObjectHandler: ((NSManagedObject) -> Bool)?`

A closure that provides a managed object for your app to insert data into.

`var resultType: NSBatchInsertRequestResultType`

The type of result that Core Data returns from this request.

Instance Property

# resultType

The type of result that Core Data returns from this request.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.1+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var resultType: NSBatchInsertRequestResultType { get set }

## Discussion

The default is `NSBatchInsertRequestResultType.statusOnly`.

## See Also

### Configuring a Request

`var dictionaryHandler: ((NSMutableDictionary) -> Bool)?`

A closure that provides a dictionary for your app to insert data into.

`var entity: NSEntityDescription?`

The managed entity to insert data into.

`var entityName: String`

The name of the managed entity to insert data into.

`var managedObjectHandler: ((NSManagedObject) -> Bool)?`

A closure that provides a managed object for your app to insert data into.

`var objectsToInsert: [[String : Any]]?`

An array of dictionaries that represents the objects to insert with the keys
as attribute names and their assigned values.

