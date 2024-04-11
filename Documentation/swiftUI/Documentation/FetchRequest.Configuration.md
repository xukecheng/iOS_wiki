Instance Property

# nsPredicate

The request’s predicate.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    var nsPredicate: NSPredicate?

## Discussion

Set this configuration value to cause a `FetchRequest` to execute a fetch with
a new predicate.

Access this value of a `FetchRequest.Configuration` structure for a given
request by using the `nsPredicate` property on the associated `FetchedResults`
instance, either directly or through a `Binding`.

Instance Property

# sortDescriptors

The request’s sort descriptors, accessed as value types.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    var sortDescriptors: [SortDescriptor<Result>] { get set }

Available when `Result` inherits `NSManagedObject`.

## Discussion

Set this configuration value to cause a `FetchRequest` to execute a fetch with
a new collection of `SortDescriptor` instances. If you want to use
`NSSortDescriptor` instances, set `nsSortDescriptors` instead.

Access this value of a `FetchRequest.Configuration` structure for a given
request by using the `sortDescriptors` property on the associated
`FetchedResults` instance, either directly or through a `Binding`.

## See Also

### Setting sort descriptors

`var nsSortDescriptors: [NSSortDescriptor]`

The request’s sort descriptors, accessed as reference types.

Instance Property

# nsSortDescriptors

The request’s sort descriptors, accessed as reference types.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    var nsSortDescriptors: [NSSortDescriptor]

## Discussion

Set this configuration value to cause a `FetchRequest` to execute a fetch with
a new collection of `NSSortDescriptor` instances. If you want to use
`SortDescriptor` instances, set `sortDescriptors` instead.

Access this value of a `FetchRequest.Configuration` structure for a given
request by using the `nsSortDescriptors` property on the associated
`FetchedResults` instance, either directly or through a `Binding`.

## See Also

### Setting sort descriptors

`var sortDescriptors: [SortDescriptor<Result>]`

The request’s sort descriptors, accessed as value types.

Available when `Result` inherits `NSManagedObject`.

