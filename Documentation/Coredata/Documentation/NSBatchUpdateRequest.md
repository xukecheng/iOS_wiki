Initializer

# init(entity:)

Creates a batch-update request for a managed entity.

iOS 8.0+  iPadOS 8.0+  macOS 10.10+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    init(entity: NSEntityDescription)

##  Parameters

`entity`

    

The managed entity to update data for.

## See Also

### Creating a Request

`init(entityName: String)`

Creates a batch-update request for a named managed entity.

Initializer

# init(entityName:)

Creates a batch-update request for a named managed entity.

iOS 8.0+  iPadOS 8.0+  macOS 10.10+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    init(entityName: String)

##  Parameters

`entityName`

    

The name of the managed entity to update data for.

## See Also

### Creating a Request

`init(entity: NSEntityDescription)`

Creates a batch-update request for a managed entity.

Instance Property

# entity

The managed entity to update data for.

iOS 8.0+  iPadOS 8.0+  macOS 10.10+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var entity: NSEntityDescription { get }

## See Also

### Configuring a Request

`var entityName: String`

The name of the managed entity to update data for.

`var includesSubentities: Bool`

A Boolean value that indicates whether to update subentities.

`var predicate: NSPredicate?`

A predicate that identifies the objects to update.

`var propertiesToUpdate: [AnyHashable : Any]?`

A dictionary of property description pairs that describe the updates.

`var resultType: NSBatchUpdateRequestResultType`

The type of result that Core Data returns from the request.

Instance Property

# entityName

The name of the managed entity to update data for.

iOS 8.0+  iPadOS 8.0+  macOS 10.10+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var entityName: String { get }

## See Also

### Configuring a Request

`var entity: NSEntityDescription`

The managed entity to update data for.

`var includesSubentities: Bool`

A Boolean value that indicates whether to update subentities.

`var predicate: NSPredicate?`

A predicate that identifies the objects to update.

`var propertiesToUpdate: [AnyHashable : Any]?`

A dictionary of property description pairs that describe the updates.

`var resultType: NSBatchUpdateRequestResultType`

The type of result that Core Data returns from the request.

Instance Property

# includesSubentities

A Boolean value that indicates whether to update subentities.

iOS 8.0+  iPadOS 8.0+  macOS 10.10+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var includesSubentities: Bool { get set }

## Discussion

The default value is `true`.

## See Also

### Configuring a Request

`var entity: NSEntityDescription`

The managed entity to update data for.

`var entityName: String`

The name of the managed entity to update data for.

`var predicate: NSPredicate?`

A predicate that identifies the objects to update.

`var propertiesToUpdate: [AnyHashable : Any]?`

A dictionary of property description pairs that describe the updates.

`var resultType: NSBatchUpdateRequestResultType`

The type of result that Core Data returns from the request.

Instance Property

# predicate

A predicate that identifies the objects to update.

iOS 8.0+  iPadOS 8.0+  macOS 10.10+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var predicate: NSPredicate? { get set }

## See Also

### Configuring a Request

`var entity: NSEntityDescription`

The managed entity to update data for.

`var entityName: String`

The name of the managed entity to update data for.

`var includesSubentities: Bool`

A Boolean value that indicates whether to update subentities.

`var propertiesToUpdate: [AnyHashable : Any]?`

A dictionary of property description pairs that describe the updates.

`var resultType: NSBatchUpdateRequestResultType`

The type of result that Core Data returns from the request.

Instance Property

# propertiesToUpdate

A dictionary of property description pairs that describe the updates.

iOS 8.0+  iPadOS 8.0+  macOS 10.10+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var propertiesToUpdate: [AnyHashable : Any]? { get set }

## Discussion

The dictionary keys are either `NSPropertyDescription` objects or strings that
identify the property name.

The dictionary values are either a constant value or an `NSExpression` that
evaluates to a scalar value.

## See Also

### Configuring a Request

`var entity: NSEntityDescription`

The managed entity to update data for.

`var entityName: String`

The name of the managed entity to update data for.

`var includesSubentities: Bool`

A Boolean value that indicates whether to update subentities.

`var predicate: NSPredicate?`

A predicate that identifies the objects to update.

`var resultType: NSBatchUpdateRequestResultType`

The type of result that Core Data returns from the request.

Instance Property

# resultType

The type of result that Core Data returns from the request.

iOS 8.0+  iPadOS 8.0+  macOS 10.10+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var resultType: NSBatchUpdateRequestResultType { get set }

## See Also

### Configuring a Request

`var entity: NSEntityDescription`

The managed entity to update data for.

`var entityName: String`

The name of the managed entity to update data for.

`var includesSubentities: Bool`

A Boolean value that indicates whether to update subentities.

`var predicate: NSPredicate?`

A predicate that identifies the objects to update.

`var propertiesToUpdate: [AnyHashable : Any]?`

A dictionary of property description pairs that describe the updates.

