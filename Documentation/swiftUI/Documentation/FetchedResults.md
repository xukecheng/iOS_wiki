Instance Property

# nsPredicate

The request’s predicate.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    var nsPredicate: NSPredicate? { get nonmutating set }

## Discussion

Set this value to cause the associated `FetchRequest` to execute a fetch with
a new predicate, producing an updated collection of results.

## See Also

### Configuring the associated fetch request

`var sortDescriptors: [SortDescriptor<Result>]`

The request’s sort descriptors, accessed as value types.

Available when `Result` inherits `NSManagedObject`.

`var nsSortDescriptors: [NSSortDescriptor]`

The request’s sort descriptors, accessed as reference types.

Instance Property

# sortDescriptors

The request’s sort descriptors, accessed as value types.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    var sortDescriptors: [SortDescriptor<Result>] { get nonmutating set }

Available when `Result` inherits `NSManagedObject`.

## Discussion

Set this value to cause the associated `FetchRequest` to execute a fetch with
a new collection of `SortDescriptor` instances. The order of entities stored
in the results collection may change as a result.

If you want to use `NSSortDescriptor` instances, set `nsSortDescriptors`
instead.

## See Also

### Configuring the associated fetch request

`var nsPredicate: NSPredicate?`

The request’s predicate.

`var nsSortDescriptors: [NSSortDescriptor]`

The request’s sort descriptors, accessed as reference types.

Instance Property

# nsSortDescriptors

The request’s sort descriptors, accessed as reference types.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    var nsSortDescriptors: [NSSortDescriptor] { get nonmutating set }

## Discussion

Set this value to cause the associated `FetchRequest` to execute a fetch with
a new collection of `NSSortDescriptor` instances. The order of managed objects
stored in the results collection may change as a result.

If you want to use `SortDescriptor` instances, set `sortDescriptors` instead.

## See Also

### Configuring the associated fetch request

`var nsPredicate: NSPredicate?`

The request’s predicate.

`var sortDescriptors: [SortDescriptor<Result>]`

The request’s sort descriptors, accessed as value types.

Available when `Result` inherits `NSManagedObject`.

Instance Property

# startIndex

The index of the first entity in the results collection.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var startIndex: Int { get }

## See Also

### Getting indices

`var endIndex: Int`

The index that’s one greater than the last valid subscript argument.

Instance Property

# endIndex

The index that’s one greater than the last valid subscript argument.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var endIndex: Int { get }

## See Also

### Getting indices

`var startIndex: Int`

The index of the first entity in the results collection.

Instance Subscript

# subscript(_:)

Gets the entity at the specified index.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    subscript(position: Int) -> Result { get }

