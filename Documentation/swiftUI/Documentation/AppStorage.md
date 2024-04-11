Initializer

# init(wrappedValue:_:store:)

Creates a property that can read and write to a string user default.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    init(
        wrappedValue: Value,
        _ key: String,
        store: UserDefaults? = nil
    ) where Value == String

##  Parameters

`wrappedValue`

    

The default value if a string value is not specified for the given key.

`key`

    

The key to read and write the value to in the user defaults store.

`store`

    

The user defaults store to read and write to. A value of `nil` will use the
user default store from the environment.

## See Also

### Storing a value

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

Initializer

# init(wrappedValue:_:store:)

Creates a property that can read and write to an integer user default,
transforming that to `RawRepresentable` data type.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    init(
        wrappedValue: Value,
        _ key: String,
        store: UserDefaults? = nil
    ) where Value : RawRepresentable, Value.RawValue == Int

##  Parameters

`wrappedValue`

    

The default value if an integer value is not specified for the given key.

`key`

    

The key to read and write the value to in the user defaults store.

`store`

    

The user defaults store to read and write to. A value of `nil` will use the
user default store from the environment.

## Discussion

A common usage is with enumerations:

enum MyEnum: Int { case a case b case c } struct MyView: View {
@AppStorage(“MyEnumValue”) private var value = MyEnum.a var body: some View {
… } }

## See Also

### Storing a value

`init(wrappedValue: Value, String, store: UserDefaults?)`

Creates a property that can read and write to a string user default.

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

Initializer

# init(wrappedValue:_:store:)

Creates a property that can read and write to a user default as data.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    init(
        wrappedValue: Value,
        _ key: String,
        store: UserDefaults? = nil
    ) where Value == Data

##  Parameters

`wrappedValue`

    

The default value if a data value is not specified for the given key.

`key`

    

The key to read and write the value to in the user defaults store.

`store`

    

The user defaults store to read and write to. A value of `nil` will use the
user default store from the environment.

## Discussion

Avoid storing large data blobs in user defaults, such as image data, as it can
negatively affect performance of your app. On tvOS, a
`NSUserDefaultsSizeLimitExceededNotification` notification is posted if the
total user default size reaches 512kB.

## See Also

### Storing a value

`init(wrappedValue: Value, String, store: UserDefaults?)`

Creates a property that can read and write to a string user default.

`init(wrappedValue: Value, String, store: UserDefaults?)`

Creates a property that can read and write to an integer user default,
transforming that to `RawRepresentable` data type.

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

Initializer

# init(wrappedValue:_:store:)

Creates a property that can read and write to an integer user default.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    init(
        wrappedValue: Value,
        _ key: String,
        store: UserDefaults? = nil
    ) where Value == Int

##  Parameters

`wrappedValue`

    

The default value if an integer value is not specified for the given key.

`key`

    

The key to read and write the value to in the user defaults store.

`store`

    

The user defaults store to read and write to. A value of `nil` will use the
user default store from the environment.

## See Also

### Storing a value

`init(wrappedValue: Value, String, store: UserDefaults?)`

Creates a property that can read and write to a string user default.

`init(wrappedValue: Value, String, store: UserDefaults?)`

Creates a property that can read and write to an integer user default,
transforming that to `RawRepresentable` data type.

`init(wrappedValue: Value, String, store: UserDefaults?)`

Creates a property that can read and write to a user default as data.

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

Initializer

# init(wrappedValue:_:store:)

Creates a property that can read and write to a string user default,
transforming that to `RawRepresentable` data type.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    init(
        wrappedValue: Value,
        _ key: String,
        store: UserDefaults? = nil
    ) where Value : RawRepresentable, Value.RawValue == String

##  Parameters

`wrappedValue`

    

The default value if a string value is not specified for the given key.

`key`

    

The key to read and write the value to in the user defaults store.

`store`

    

The user defaults store to read and write to. A value of `nil` will use the
user default store from the environment.

## Discussion

A common usage is with enumerations:

enum MyEnum: String { case a case b case c } struct MyView: View {
@AppStorage(“MyEnumValue”) private var value = MyEnum.a var body: some View {
… } }

## See Also

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

Initializer

# init(wrappedValue:_:store:)

Creates a property that can read and write to a url user default.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    init(
        wrappedValue: Value,
        _ key: String,
        store: UserDefaults? = nil
    ) where Value == URL

##  Parameters

`wrappedValue`

    

The default value if a url value is not specified for the given key.

`key`

    

The key to read and write the value to in the user defaults store.

`store`

    

The user defaults store to read and write to. A value of `nil` will use the
user default store from the environment.

## See Also

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

Creates a property that can read and write to a double user default.

`init(wrappedValue: Value, String, store: UserDefaults?)`

Creates a property that can read and write to a boolean user default.

`init<RowValue>(wrappedValue: Value, String, store: UserDefaults?)`

Creates a property that can save and restore table column state.

`init(wrappedValue: Value, String, store: UserDefaults?)`

Creates a property that can read and write to a user default as data via
`PersistentIdentifier`.

Initializer

# init(wrappedValue:_:store:)

Creates a property that can read and write to a double user default.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    init(
        wrappedValue: Value,
        _ key: String,
        store: UserDefaults? = nil
    ) where Value == Double

##  Parameters

`wrappedValue`

    

The default value if a double value is not specified for the given key.

`key`

    

The key to read and write the value to in the user defaults store.

`store`

    

The user defaults store to read and write to. A value of `nil` will use the
user default store from the environment.

## See Also

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

Creates a property that can read and write to a boolean user default.

`init<RowValue>(wrappedValue: Value, String, store: UserDefaults?)`

Creates a property that can save and restore table column state.

`init(wrappedValue: Value, String, store: UserDefaults?)`

Creates a property that can read and write to a user default as data via
`PersistentIdentifier`.

Initializer

# init(wrappedValue:_:store:)

Creates a property that can read and write to a boolean user default.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    init(
        wrappedValue: Value,
        _ key: String,
        store: UserDefaults? = nil
    ) where Value == Bool

##  Parameters

`wrappedValue`

    

The default value if a boolean value is not specified for the given key.

`key`

    

The key to read and write the value to in the user defaults store.

`store`

    

The user defaults store to read and write to. A value of `nil` will use the
user default store from the environment.

## See Also

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

`init<RowValue>(wrappedValue: Value, String, store: UserDefaults?)`

Creates a property that can save and restore table column state.

`init(wrappedValue: Value, String, store: UserDefaults?)`

Creates a property that can read and write to a user default as data via
`PersistentIdentifier`.

Initializer

# init(wrappedValue:_:store:)

Creates a property that can save and restore table column state.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    init<RowValue>(
        wrappedValue: Value = TableColumnCustomization<RowValue>(),
        _ key: String,
        store: UserDefaults? = nil
    ) where Value == TableColumnCustomization<RowValue>, RowValue : Identifiable

##  Parameters

`wrappedValue`

    

The default value if table column state is not available for the given key.

`key`

    

The key to read and write the value to in the user defaults store.

`store`

    

The user defaults store to read and write to. A value of `nil` will use the
user default store from the environment.

## Discussion

Table column state is typically not bound from a table directly to
`AppStorage`, but instead indirecting through `State` or `SceneStorage`, and
using the app storage value as its initial value kept up to date on changes to
the direct backing.

## See Also

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

`init(wrappedValue: Value, String, store: UserDefaults?)`

Creates a property that can read and write to a user default as data via
`PersistentIdentifier`.

Initializer

# init(wrappedValue:_:store:)

Creates a property that can read and write to a user default as data via
`PersistentIdentifier`.

SwiftData  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  tvOS 17.0+  watchOS
10.0+

    
    
    init(
        wrappedValue: Value,
        _ key: String,
        store: UserDefaults? = nil
    ) where Value == PersistentIdentifier

##  Parameters

`wrappedValue`

    

The default value if a data value is not specified for the given key.

`key`

    

The key to read and write the value to in the user defaults store.

`store`

    

The user defaults store to read and write to. A value of `nil` will use the
user default store from the environment.

## Discussion

Use this property wrapper when the wrapped persistent identifier is known to
always be non-optional. For storing optional persistent identifiers, use
`AppStorage/init(_:store:)` instead.

## See Also

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

Initializer

# init(_:store:)

Creates a property that can read and write an Optional integer user default.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    init(
        _ key: String,
        store: UserDefaults? = nil
    ) where Value == Int?

Available when `Value` conforms to `ExpressibleByNilLiteral`.

##  Parameters

`key`

    

The key to read and write the value to in the user defaults store.

`store`

    

The user defaults store to read and write to. A value of `nil` will use the
user default store from the environment.

## Discussion

Defaults to nil if there is no restored value.

## See Also

### Storing an optional value

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

Initializer

# init(_:store:)

Creates a property that can read and write an Optional string user default.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    init(
        _ key: String,
        store: UserDefaults? = nil
    ) where Value == String?

Available when `Value` conforms to `ExpressibleByNilLiteral`.

##  Parameters

`key`

    

The key to read and write the value to in the user defaults store.

`store`

    

The user defaults store to read and write to. A value of `nil` will use the
user default store from the environment.

## Discussion

Defaults to nil if there is no restored value.

## See Also

### Storing an optional value

`init(String, store: UserDefaults?)`

Creates a property that can read and write an Optional integer user default.

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

Initializer

# init(_:store:)

Creates a property that can read and write an Optional double user default.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    init(
        _ key: String,
        store: UserDefaults? = nil
    ) where Value == Double?

Available when `Value` conforms to `ExpressibleByNilLiteral`.

##  Parameters

`key`

    

The key to read and write the value to in the user defaults store.

`store`

    

The user defaults store to read and write to. A value of `nil` will use the
user default store from the environment.

## Discussion

Defaults to nil if there is no restored value.

## See Also

### Storing an optional value

`init(String, store: UserDefaults?)`

Creates a property that can read and write an Optional integer user default.

Available when `Value` conforms to `ExpressibleByNilLiteral`.

`init(String, store: UserDefaults?)`

Creates a property that can read and write an Optional string user default.

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

Initializer

# init(_:store:)

Creates a property that can save and restore an Optional integer, transforming
it to an Optional `RawRepresentable` data type.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    init<R>(
        _ key: String,
        store: UserDefaults? = nil
    ) where Value == R?, R : RawRepresentable, R.RawValue == Int

##  Parameters

`key`

    

The key to read and write the value to in the user defaults store.

`store`

    

The user defaults store to read and write to. A value of `nil` will use the
user default store from the environment.

## Discussion

Defaults to nil if there is no restored value

A common usage is with enumerations:

## See Also

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

Initializer

# init(_:store:)

Creates a property that can save and restore an Optional string, transforming
it to an Optional `RawRepresentable` data type.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    init<R>(
        _ key: String,
        store: UserDefaults? = nil
    ) where Value == R?, R : RawRepresentable, R.RawValue == String

##  Parameters

`key`

    

The key to read and write the value to in the user defaults store.

`store`

    

The user defaults store to read and write to. A value of `nil` will use the
user default store from the environment.

## Discussion

Defaults to nil if there is no restored value

A common usage is with enumerations:

## See Also

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

Initializer

# init(_:store:)

Creates a property that can read and write an Optional data user default.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    init(
        _ key: String,
        store: UserDefaults? = nil
    ) where Value == Data?

Available when `Value` conforms to `ExpressibleByNilLiteral`.

##  Parameters

`key`

    

The key to read and write the value to in the user defaults store.

`store`

    

The user defaults store to read and write to. A value of `nil` will use the
user default store from the environment.

## Discussion

Defaults to nil if there is no restored value.

## See Also

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

Creates a property that can read and write an Optional boolean user default.

Available when `Value` conforms to `ExpressibleByNilLiteral`.

`init(String, store: UserDefaults?)`

Creates a property that can read and write an Optional URL user default.

Available when `Value` conforms to `ExpressibleByNilLiteral`.

`init(String, store: UserDefaults?)`

Creates a property that can read and write an Optional data user default via
`PersistentIdentifier`.

Initializer

# init(_:store:)

Creates a property that can read and write an Optional boolean user default.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    init(
        _ key: String,
        store: UserDefaults? = nil
    ) where Value == Bool?

Available when `Value` conforms to `ExpressibleByNilLiteral`.

##  Parameters

`key`

    

The key to read and write the value to in the user defaults store.

`store`

    

The user defaults store to read and write to. A value of `nil` will use the
user default store from the environment.

## Discussion

Defaults to nil if there is no restored value.

## See Also

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

Creates a property that can read and write an Optional URL user default.

Available when `Value` conforms to `ExpressibleByNilLiteral`.

`init(String, store: UserDefaults?)`

Creates a property that can read and write an Optional data user default via
`PersistentIdentifier`.

Initializer

# init(_:store:)

Creates a property that can read and write an Optional URL user default.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    init(
        _ key: String,
        store: UserDefaults? = nil
    ) where Value == URL?

Available when `Value` conforms to `ExpressibleByNilLiteral`.

##  Parameters

`key`

    

The key to read and write the value to in the user defaults store.

`store`

    

The user defaults store to read and write to. A value of `nil` will use the
user default store from the environment.

## Discussion

Defaults to nil if there is no restored value.

## See Also

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

Creates a property that can read and write an Optional data user default via
`PersistentIdentifier`.

Initializer

# init(_:store:)

Creates a property that can read and write an Optional data user default via
`PersistentIdentifier`.

SwiftData  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  tvOS 17.0+  watchOS
10.0+

    
    
    init(
        _ key: String,
        store: UserDefaults? = nil
    ) where Value == PersistentIdentifier?

##  Parameters

`key`

    

The key to read and write the value to in the user defaults store.

`store`

    

The user defaults store to read and write to. A value of `nil` will use the
user default store from the environment.

## Discussion

Defaults to `nil` if there is no restored value.

## See Also

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

Instance Property

# wrappedValue

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    var wrappedValue: Value { get nonmutating set }

## See Also

### Getting the value

`var projectedValue: Binding<Value>`

Instance Property

# projectedValue

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    var projectedValue: Binding<Value> { get }

## See Also

### Getting the value

`var wrappedValue: Value`

