Instance Property

# sectionIdentifier

The request’s section identifier key path.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    var sectionIdentifier: KeyPath<Result, SectionIdentifier>

## Discussion

Set this configuration value to cause a `SectionedFetchRequest` to execute a
fetch with a new section identifier. You can’t change the section identifier
type without creating a new fetch request. Use care to coordinate section and
sort updates, as described in `SectionedFetchRequest.Configuration`.

Access this value for a given request by using the `sectionIdentifier`
property on the associated `SectionedFetchResults` instance, either directly
or with a `Binding`.

Instance Property

# nsPredicate

The request’s predicate.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    var nsPredicate: NSPredicate?

## Discussion

Set this configuration value to cause a `SectionedFetchRequest` to execute a
fetch with a new predicate.

Access this value for a given request by using the `nsPredicate` property on
the associated `SectionedFetchResults` instance, either directly or with a
`Binding`.

Instance Property

# sortDescriptors

The request’s sort descriptors, accessed as value types.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    var sortDescriptors: [SortDescriptor<Result>] { get set }

Available when `SectionIdentifier` conforms to `Hashable` and `Result`
inherits `NSManagedObject`.

## Discussion

Set this configuration value to cause a `SectionedFetchRequest` to execute a
fetch with a new collection of `SortDescriptor` instances. If you want to use
`NSSortDescriptor` instances, set `nsSortDescriptors` instead. Use care to
coordinate section and sort updates, as described in
`SectionedFetchRequest.Configuration`.

Access this value for a given request by using the `sortDescriptors` property
on the associated `SectionedFetchResults` instance, either directly or with a
`Binding`.

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

Set this configuration value to cause a `SectionedFetchRequest` to execute a
fetch with a new collection of `NSSortDescriptor` instances. If you want to
use `SortDescriptor` instances, set `sortDescriptors` instead. Use care to
coordinate section and sort updates, as described in
`SectionedFetchRequest.Configuration`.

Access this value for a given request by using the `nsSortDescriptors`
property on the associated `SectionedFetchResults` instance, either directly
or with a `Binding`.

## See Also

### Setting sort descriptors

`var sortDescriptors: [SortDescriptor<Result>]`

The request’s sort descriptors, accessed as value types.

Available when `SectionIdentifier` conforms to `Hashable` and `Result`
inherits `NSManagedObject`.

