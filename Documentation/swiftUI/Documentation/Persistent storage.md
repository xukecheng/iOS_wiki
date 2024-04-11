Instance Method

# defaultAppStorage(_:)

The default store used by `AppStorage` contained within the view.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    func defaultAppStorage(_ store: UserDefaults) -> some View
    

##  Parameters

`store`

    

The user defaults to use as the default store for `AppStorage`.

## Discussion

If unspecified, the default store for a view hierarchy is
`UserDefaults.standard`, but can be set a to a custom one. For example,
sharing defaults between an app and an extension can override the default
store to one created with `UserDefaults.init(suiteName:_)`.

## See Also

### Saving state across app launches

Restoring Your App’s State with SwiftUI

Provide app continuity for users by preserving their current activities.

`struct AppStorage`

A property wrapper type that reflects a value from `UserDefaults` and
invalidates a view on a change in value in that user default.

`struct SceneStorage`

A property wrapper type that reads and writes to persisted, per-scene storage.

Structure

# AppStorage

A property wrapper type that reflects a value from `UserDefaults` and
invalidates a view on a change in value in that user default.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    @frozen @propertyWrapper
    struct AppStorage<Value>

## Topics

### Storing a value

`init(wrappedValue: Value, String, store: UserDefaults?)`

Creates a property that can read and write to a string user default.

`init(wrappedValue: Value, String, store: UserDefaults?)`

Creates a property that can read and write to an integer user default,
transforming that to `RawRepresentable` data type.

`init(wrappedValue: Value, String, store: UserDefaults?)`

Creates a property that can read and write to a user default as data.

`init(wrappedValue: Value, String, store: UserDefaults?)`

Creates a property that can read and write to an integer user default.

`init(wrappedValue: Value, String, store: UserDefaults?)`

Creates a property that can read and write to a string user default,
transforming that to `RawRepresentable` data type.

`init(wrappedValue: Value, String, store: UserDefaults?)`

Creates a property that can read and write to a url user default.

`init(wrappedValue: Value, String, store: UserDefaults?)`

Creates a property that can read and write to a double user default.

`init(wrappedValue: Value, String, store: UserDefaults?)`

Creates a property that can read and write to a boolean user default.

`init<RowValue>(wrappedValue: Value, String, store: UserDefaults?)`

Creates a property that can save and restore table column state.

`init(wrappedValue: Value, String, store: UserDefaults?)`

Creates a property that can read and write to a user default as data via
`PersistentIdentifier`.

### Storing an optional value

`init(String, store: UserDefaults?)`

Creates a property that can read and write an Optional integer user default.

Available when `Value` conforms to `ExpressibleByNilLiteral`.

`init(String, store: UserDefaults?)`

Creates a property that can read and write an Optional string user default.

Available when `Value` conforms to `ExpressibleByNilLiteral`.

`init(String, store: UserDefaults?)`

Creates a property that can read and write an Optional double user default.

Available when `Value` conforms to `ExpressibleByNilLiteral`.

`init<R>(String, store: UserDefaults?)`

Creates a property that can save and restore an Optional integer, transforming
it to an Optional `RawRepresentable` data type.

`init<R>(String, store: UserDefaults?)`

Creates a property that can save and restore an Optional string, transforming
it to an Optional `RawRepresentable` data type.

`init(String, store: UserDefaults?)`

Creates a property that can read and write an Optional data user default.

Available when `Value` conforms to `ExpressibleByNilLiteral`.

`init(String, store: UserDefaults?)`

Creates a property that can read and write an Optional boolean user default.

Available when `Value` conforms to `ExpressibleByNilLiteral`.

`init(String, store: UserDefaults?)`

Creates a property that can read and write an Optional URL user default.

Available when `Value` conforms to `ExpressibleByNilLiteral`.

`init(String, store: UserDefaults?)`

Creates a property that can read and write an Optional data user default via
`PersistentIdentifier`.

### Getting the value

`var wrappedValue: Value`

`var projectedValue: Binding<Value>`

## Relationships

### Conforms To

  * `DynamicProperty`

## See Also

### Saving state across app launches

Restoring Your App’s State with SwiftUI

Provide app continuity for users by preserving their current activities.

`func defaultAppStorage(UserDefaults) -> some View`

The default store used by `AppStorage` contained within the view.

`struct SceneStorage`

A property wrapper type that reads and writes to persisted, per-scene storage.

Structure

# SceneStorage

A property wrapper type that reads and writes to persisted, per-scene storage.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    @frozen @propertyWrapper
    struct SceneStorage<Value>

## Overview

You use `SceneStorage` when you need automatic state restoration of the value.
`SceneStorage` works very similar to `State`, except its initial value is
restored by the system if it was previously saved, and the value is shared
with other `SceneStorage` variables in the same scene.

The system manages the saving and restoring of `SceneStorage` on your behalf.
The underlying data that backs `SceneStorage` is not available to you, so you
must access it via the `SceneStorage` property wrapper. The system makes no
guarantees as to when and how often the data will be persisted.

Each `Scene` has its own notion of `SceneStorage`, so data is not shared
between scenes.

Ensure that the data you use with `SceneStorage` is lightweight. Data of a
large size, such as model data, should not be stored in `SceneStorage`, as
poor performance may result.

If the `Scene` is explicitly destroyed (e.g. the switcher snapshot is
destroyed on iPadOS or the window is closed on macOS), the data is also
destroyed. Do not use `SceneStorage` with sensitive data.

## Topics

### Storing a value

`init(wrappedValue: Value, String)`

Creates a property that can save and restore a URL.

`init(wrappedValue: Value, String)`

Creates a property that can save and restore an integer.

`init(wrappedValue: Value, String)`

Creates a property that can save and restore a double.

`init(wrappedValue: Value, String)`

Creates a property that can save and restore a string.

`init(wrappedValue: Value, String)`

Creates a property that can save and restore a boolean.

`init(wrappedValue: Value, String)`

Creates a property that can save and restore a string, transforming it to a
`RawRepresentable` data type.

`init(wrappedValue: Value, String)`

Creates a property that can save and restore data.

`init(wrappedValue: Value, String)`

Creates a property that can save and restore an integer, transforming it to a
`RawRepresentable` data type.

`init<RowValue>(wrappedValue: Value, String)`

Creates a property that can save and restore table column state.

`init(wrappedValue: Value, String)`

Creates a property that can save and restore a `PersistentIdentifier`.

### Storing an optional value

`init(String)`

Creates a property that can save and restore an Optional string.

Available when `Value` conforms to `ExpressibleByNilLiteral`.

`init<R>(String)`

Creates a property that can save and restore an Optional integer, transforming
it to an Optional `RawRepresentable` data type.

`init(String)`

Creates a property that can save and restore an Optional double.

Available when `Value` conforms to `ExpressibleByNilLiteral`.

`init(String)`

Creates a property that can save and restore an Optional boolean.

Available when `Value` conforms to `ExpressibleByNilLiteral`.

`init(String)`

Creates a property that can save and restore an Optional data.

Available when `Value` conforms to `ExpressibleByNilLiteral`.

`init(String)`

Creates a property that can save and restore an Optional URL.

Available when `Value` conforms to `ExpressibleByNilLiteral`.

`init(String)`

Creates a property that can save and restore an Optional integer.

Available when `Value` conforms to `ExpressibleByNilLiteral`.

`init<R>(String)`

Creates a property that can save and restore an Optional string, transforming
it to an Optional `RawRepresentable` data type.

`init(String)`

Creates a property that can read and write an Optional data user default via
`PersistentIdentifier`.

### Getting the value

`var wrappedValue: Value`

The underlying value referenced by the state variable.

`var projectedValue: Binding<Value>`

A binding to the state value.

## Relationships

### Conforms To

  * `DynamicProperty`

## See Also

### Saving state across app launches

Restoring Your App’s State with SwiftUI

Provide app continuity for users by preserving their current activities.

`func defaultAppStorage(UserDefaults) -> some View`

The default store used by `AppStorage` contained within the view.

`struct AppStorage`

A property wrapper type that reflects a value from `UserDefaults` and
invalidates a view on a change in value in that user default.

Instance Property

# managedObjectContext

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var managedObjectContext: NSManagedObjectContext { get set }

## See Also

### Accessing Core Data

Loading and Displaying a Large Data Feed

Consume data in the background, and lower memory use by batching imports and
preventing duplicate records.

`struct FetchRequest`

A property wrapper type that retrieves entities from a Core Data persistent
store.

`struct FetchedResults`

A collection of results retrieved from a Core Data store.

`struct SectionedFetchRequest`

A property wrapper type that retrieves entities, grouped into sections, from a
Core Data persistent store.

`struct SectionedFetchResults`

A collection of results retrieved from a Core Data persistent store, grouped
into sections.

Structure

# FetchRequest

A property wrapper type that retrieves entities from a Core Data persistent
store.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @MainActor @propertyWrapper
    struct FetchRequest<Result> where Result : NSFetchRequestResult

## Overview

Use a `FetchRequest` property wrapper to declare a `FetchedResults` property
that provides a collection of Core Data managed objects to a SwiftUI view. The
request infers the entity type from the `Result` placeholder type that you
specify. Condition the request with an optional predicate and sort
descriptors. For example, you can create a request to list all `Quake` managed
objects that the Loading and Displaying a Large Data Feed sample code project
defines to store earthquake data, sorted by their `time` property:

Alternatively, when you need more flexibility, you can initialize the request
with a configured `NSFetchRequest` instance:

Always declare properties that have a fetch request wrapper as private. This
lets the compiler help you avoid accidentally setting the property from the
memberwise initializer of the enclosing view.

The fetch request and its results use the managed object context stored in the
environment, which you can access using the `managedObjectContext` environment
value. To support user interface activity, you typically rely on the
`viewContext` property of a shared `NSPersistentContainer` instance. For
example, you can set a context on your top level content view using a shared
container that you define as part of your model:

When you need to dynamically change the predicate or sort descriptors, access
the request’s `FetchRequest.Configuration` structure. To create a request that
groups the fetched results according to a characteristic that they share, use
`SectionedFetchRequest` instead.

## Topics

### Creating a fetch request

`init(sortDescriptors: [SortDescriptor<Result>], predicate: NSPredicate?,
animation: Animation?)`

Creates a fetch request based on a predicate and value type sort parameters.

Available when `Result` inherits `NSManagedObject`.

`init(sortDescriptors: [NSSortDescriptor], predicate: NSPredicate?, animation:
Animation?)`

Creates a fetch request based on a predicate and reference type sort
parameters.

Available when `Result` inherits `NSManagedObject`.

`init(entity: NSEntityDescription, sortDescriptors: [NSSortDescriptor],
predicate: NSPredicate?, animation: Animation?)`

Creates a fetch request for a specified entity description, based on a
predicate and sort parameters.

Available when `Result` conforms to `NSFetchRequestResult`.

### Creating a fully configured fetch request

`init(fetchRequest: NSFetchRequest<Result>, animation: Animation?)`

Creates a fully configured fetch request that uses the specified animation
when updating results.

Available when `Result` conforms to `NSFetchRequestResult`.

`init(fetchRequest: NSFetchRequest<Result>, transaction: Transaction)`

Creates a fully configured fetch request that uses the specified transaction
when updating results.

Available when `Result` conforms to `NSFetchRequestResult`.

### Configuring a request dynamically

`struct Configuration`

The request’s configurable properties.

`var projectedValue: Binding<FetchRequest<Result>.Configuration>`

A binding to the request’s mutable configuration properties.

### Getting the fetched results

`func update()`

Updates the fetched results.

Available when `Result` conforms to `NSFetchRequestResult`.

`var wrappedValue: FetchedResults<Result>`

The fetched results of the fetch request.

### Default Implementations

API Reference

DynamicProperty Implementations

## Relationships

### Conforms To

  * `DynamicProperty`

Conforms when `Result` conforms to `NSFetchRequestResult`.

## See Also

### Accessing Core Data

Loading and Displaying a Large Data Feed

Consume data in the background, and lower memory use by batching imports and
preventing duplicate records.

`var managedObjectContext: NSManagedObjectContext`

`struct FetchedResults`

A collection of results retrieved from a Core Data store.

`struct SectionedFetchRequest`

A property wrapper type that retrieves entities, grouped into sections, from a
Core Data persistent store.

`struct SectionedFetchResults`

A collection of results retrieved from a Core Data persistent store, grouped
into sections.

Structure

# FetchedResults

A collection of results retrieved from a Core Data store.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    struct FetchedResults<Result> where Result : NSFetchRequestResult

## Overview

Use a `FetchedResults` instance to show or edit Core Data managed objects in
your app’s user interface. You request a particular set of results by
specifying a `Result` type as the entity type, and annotating the fetched
results property declaration with a `FetchRequest` property wrapper. For
example, you can create a request to list all `Quake` managed objects that the
Loading and Displaying a Large Data Feed sample code project defines to store
earthquake data, sorted by their `time` property:

The results instance conforms to `RandomAccessCollection`, so you access it
like any other collection. For example, you can create a `List` that iterates
over all the results:

When you need to dynamically change the request’s predicate or sort
descriptors, set the result instance’s `nsPredicate` and `sortDescriptors` or
`nsSortDescriptors` properties, respectively.

The fetch request and its results use the managed object context stored in the
environment, which you can access using the `managedObjectContext` environment
value. To support user interface activity, you typically rely on the
`viewContext` property of a shared `NSPersistentContainer` instance. For
example, you can set a context on your top level content view using a
container that you define as part of your model:

## Topics

### Configuring the associated fetch request

`var nsPredicate: NSPredicate?`

The request’s predicate.

`var sortDescriptors: [SortDescriptor<Result>]`

The request’s sort descriptors, accessed as value types.

Available when `Result` inherits `NSManagedObject`.

`var nsSortDescriptors: [NSSortDescriptor]`

The request’s sort descriptors, accessed as reference types.

### Getting indices

`var startIndex: Int`

The index of the first entity in the results collection.

`var endIndex: Int`

The index that’s one greater than the last valid subscript argument.

### Getting results

`subscript(Int) -> Result`

Gets the entity at the specified index.

## Relationships

### Conforms To

  * `BidirectionalCollection`
  * `Collection`
  * `RandomAccessCollection`
  * `Sequence`

## See Also

### Accessing Core Data

Loading and Displaying a Large Data Feed

Consume data in the background, and lower memory use by batching imports and
preventing duplicate records.

`var managedObjectContext: NSManagedObjectContext`

`struct FetchRequest`

A property wrapper type that retrieves entities from a Core Data persistent
store.

`struct SectionedFetchRequest`

A property wrapper type that retrieves entities, grouped into sections, from a
Core Data persistent store.

`struct SectionedFetchResults`

A collection of results retrieved from a Core Data persistent store, grouped
into sections.

Structure

# SectionedFetchRequest

A property wrapper type that retrieves entities, grouped into sections, from a
Core Data persistent store.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    @MainActor @propertyWrapper
    struct SectionedFetchRequest<SectionIdentifier, Result> where SectionIdentifier : Hashable, Result : NSFetchRequestResult

## Overview

Use a `SectionedFetchRequest` property wrapper to declare a
`SectionedFetchResults` property that provides a grouped collection of Core
Data managed objects to a SwiftUI view. If you don’t need sectioning, use
`FetchRequest` instead.

Configure a sectioned fetch request with an optional predicate and sort
descriptors, and include a `sectionIdentifier` parameter to indicate how to
group the fetched results. Be sure that you choose sorting and sectioning that
work together to avoid discontiguous sections. For example, you can request a
list of earthquakes, composed of `Quake` managed objects that the Loading and
Displaying a Large Data Feed sample code project defines to store earthquake
data, sorted by time and grouped by date:

Always declare properties that have a sectioned fetch request wrapper as
private. This lets the compiler help you avoid accidentally setting the
property from the memberwise initializer of the enclosing view.

The request infers the entity type from the `Result` type that you specify,
which is `Quake` in the example above. Indicate a `SectionIdentifier` type to
declare the type found at the fetched object’s `sectionIdentifier` key path.
The section identifier type must conform to the `Hashable` protocol.

The example above depends on the `Quake` type having a `day` property that’s
either a stored or computed string. Be sure to mark any computed property with
the `@objc` attribute for it to function as a section identifier. For best
performance with large data sets, use stored properties.

The sectioned fetch request and its results use the managed object context
stored in the environment, which you can access using the
`managedObjectContext` environment value. To support user interface activity,
you typically rely on the `viewContext` property of a shared
`NSPersistentContainer` instance. For example, you can set a context on your
top-level content view using a shared container that you define as part of
your model:

When you need to dynamically change the section identifier, predicate, or sort
descriptors, access the request’s `SectionedFetchRequest.Configuration`
structure, either directly or with a binding.

## Topics

### Creating a fetch request

`init(sectionIdentifier: KeyPath<Result, SectionIdentifier>, sortDescriptors:
[SortDescriptor<Result>], predicate: NSPredicate?, animation: Animation?)`

Creates a sectioned fetch request based on a section identifier, a predicate,
and value type sort parameters.

Available when `SectionIdentifier` conforms to `Hashable` and `Result`
inherits `NSManagedObject`.

`init(sectionIdentifier: KeyPath<Result, SectionIdentifier>, sortDescriptors:
[NSSortDescriptor], predicate: NSPredicate?, animation: Animation?)`

Creates a sectioned fetch request based on a section identifier, a predicate,
and reference type sort parameters.

Available when `SectionIdentifier` conforms to `Hashable` and `Result`
inherits `NSManagedObject`.

`init(entity: NSEntityDescription, sectionIdentifier: KeyPath<Result,
SectionIdentifier>, sortDescriptors: [NSSortDescriptor], predicate:
NSPredicate?, animation: Animation?)`

Creates a sectioned fetch request for a specified entity description, based on
a section identifier, a predicate, and sort parameters.

Available when `SectionIdentifier` conforms to `Hashable` and `Result`
conforms to `NSFetchRequestResult`.

### Creating a fully configured fetch request

`init(fetchRequest: NSFetchRequest<Result>, sectionIdentifier: KeyPath<Result,
SectionIdentifier>, animation: Animation?)`

Creates a fully configured sectioned fetch request that uses the specified
animation when updating results.

Available when `SectionIdentifier` conforms to `Hashable` and `Result`
conforms to `NSFetchRequestResult`.

`init(fetchRequest: NSFetchRequest<Result>, sectionIdentifier: KeyPath<Result,
SectionIdentifier>, transaction: Transaction)`

Creates a fully configured sectioned fetch request that uses the specified
transaction when updating results.

Available when `SectionIdentifier` conforms to `Hashable` and `Result`
conforms to `NSFetchRequestResult`.

### Configuring a request dynamically

`struct Configuration`

The request’s configurable properties.

`var projectedValue: Binding<SectionedFetchRequest<SectionIdentifier,
Result>.Configuration>`

A binding to the request’s mutable configuration properties.

### Getting the fetched results

`func update()`

Updates the fetched results.

Available when `SectionIdentifier` conforms to `Hashable` and `Result`
conforms to `NSFetchRequestResult`.

`var wrappedValue: SectionedFetchResults<SectionIdentifier, Result>`

The fetched results of the fetch request.

### Default Implementations

API Reference

DynamicProperty Implementations

## Relationships

### Conforms To

  * `DynamicProperty`

Conforms when `SectionIdentifier` conforms to `Hashable` and `Result` conforms
to `NSFetchRequestResult`.

## See Also

### Accessing Core Data

Loading and Displaying a Large Data Feed

Consume data in the background, and lower memory use by batching imports and
preventing duplicate records.

`var managedObjectContext: NSManagedObjectContext`

`struct FetchRequest`

A property wrapper type that retrieves entities from a Core Data persistent
store.

`struct FetchedResults`

A collection of results retrieved from a Core Data store.

`struct SectionedFetchResults`

A collection of results retrieved from a Core Data persistent store, grouped
into sections.

Structure

# SectionedFetchResults

A collection of results retrieved from a Core Data persistent store, grouped
into sections.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    struct SectionedFetchResults<SectionIdentifier, Result> where SectionIdentifier : Hashable, Result : NSFetchRequestResult

## Overview

Use a `SectionedFetchResults` instance to show or edit Core Data managed
objects, grouped into sections, in your app’s user interface. If you don’t
need sectioning, use `FetchedResults` instead.

You request a particular set of results by annotating the fetched results
property declaration with a `SectionedFetchRequest` property wrapper. Indicate
the type of the fetched entities with a `Results` type, and the type of the
identifier that distinguishes the sections with a `SectionIdentifier` type.
For example, you can create a request to list all `Quake` managed objects that
the Loading and Displaying a Large Data Feed sample code project defines to
store earthquake data, sorted by their `time` property and grouped by a string
that represents the days when earthquakes occurred:

The `quakes` property acts as a collection of `SectionedFetchResults.Section`
instances, each containing a collection of `Quake` instances. The example
above depends on the `Quake` model object declaring both `time` and `day`
properties, either stored or computed. For best performance with large data
sets, use stored properties.

The collection of sections, as well as the collection of managed objects in
each section, conforms to the `RandomAccessCollection` protocol, so you can
access them as you would any other collection. For example, you can create
nested `ForEach` loops inside a `List` to iterate over the results:

Don’t confuse the `Section` view that you use to create a hierarchical display
with the `SectionedFetchResults.Section` instances that hold the fetched
results.

When you need to dynamically change the request’s section identifier,
predicate, or sort descriptors, set the result instance’s `sectionIdentifier`,
`nsPredicate`, and `sortDescriptors` or `nsSortDescriptors` properties,
respectively. Be sure that the sorting and sectioning work together to avoid
discontinguous sections.

The fetch request and its results use the managed object context stored in the
environment, which you can access using the `managedObjectContext` environment
value. To support user interface activity, you typically rely on the
`viewContext` property of a shared `NSPersistentContainer` instance. For
example, you can set a context on your top-level content view using a
container that you define as part of your model:

## Topics

### Configuring the associated sectioned fetch request

`var nsPredicate: NSPredicate?`

The request’s predicate.

`var sortDescriptors: [SortDescriptor<Result>]`

The request’s sort descriptors, accessed as value types.

Available when `SectionIdentifier` conforms to `Hashable` and `Result`
inherits `NSManagedObject`.

`var nsSortDescriptors: [NSSortDescriptor]`

The request’s sort descriptors, accessed as reference types.

`var sectionIdentifier: KeyPath<Result, SectionIdentifier>`

The key path that the system uses to group fetched results into sections.

`struct Section`

A collection of fetched results that share a specified identifier.

### Getting indices

`var startIndex: Int`

The index of the first section in the results collection.

`var endIndex: Int`

The index that’s one greater than that of the last section.

### Getting results

`subscript(Int) -> SectionedFetchResults<SectionIdentifier, Result>.Section`

Gets the section at the specified index.

## Relationships

### Conforms To

  * `BidirectionalCollection`
  * `Collection`
  * `RandomAccessCollection`
  * `Sequence`

## See Also

### Accessing Core Data

Loading and Displaying a Large Data Feed

Consume data in the background, and lower memory use by batching imports and
preventing duplicate records.

`var managedObjectContext: NSManagedObjectContext`

`struct FetchRequest`

A property wrapper type that retrieves entities from a Core Data persistent
store.

`struct FetchedResults`

A collection of results retrieved from a Core Data store.

`struct SectionedFetchRequest`

A property wrapper type that retrieves entities, grouped into sections, from a
Core Data persistent store.

