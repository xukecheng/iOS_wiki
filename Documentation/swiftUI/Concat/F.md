# FileDocumentConfiguration

Instance Property

# document

The current document model.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    @Binding
    var document: Document { get nonmutating set }

## Discussion

Setting a new value marks the document as having changes for later saving and
registers an undo action to restore the model to its previous value.

If `isEditable` is `false`, setting a new value has no effect because the
document is in viewing mode.

## See Also

### Getting and setting the document

`var $document: Binding<Document>`

Instance Property

# $document

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    var $document: Binding<Document> { get }

## See Also

### Getting and setting the document

`var document: Document`

The current document model.

Instance Property

# fileURL

The URL of the open file document.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    var fileURL: URL?

## See Also

### Getting document properties

`var isEditable: Bool`

A Boolean that indicates whether you can edit the document.

Instance Property

# isEditable

A Boolean that indicates whether you can edit the document.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    var isEditable: Bool

## Discussion

This value is `false` if the document is in viewing mode, or if the file is
not writable.

## See Also

### Getting document properties

`var fileURL: URL?`

The URL of the open file document.



# FileDocument

Initializer

# init(configuration:)

Creates a document and initializes it with the contents of a file.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    init(configuration: Self.ReadConfiguration) throws

**Required**

##  Parameters

`configuration`

    

Information about the file that you read document data from.

## Discussion

SwiftUI calls this initializer when someone opens a file type that matches one
of those that your document type supports. Use the `file` property of the
`configuration` input to get document’s data. Deserialize the data, and store
it in your document’s data structure:

The above example assumes that you define `Model` to contain the document’s
data, that `Model` conforms to the `Codable` protocol, and that you store a
`model` property of that type inside your document.

Note

SwiftUI calls this method on a background thread. Don’t make user interface
changes from that thread.

## See Also

### Reading a document

`static var readableContentTypes: [UTType]`

The file and data types that the document reads from.

**Required**

` typealias ReadConfiguration`

The configuration for reading document contents.

Type Property

# readableContentTypes

The file and data types that the document reads from.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    static var readableContentTypes: [UTType] { get }

**Required**

## Discussion

Define this list to indicate the content types that your document can read. By
default, SwiftUI assumes that your document can also write the same set of
content types. If you need to indicate a different set of types for writing
files, define the `writableContentTypes` property in addition to this
property.

## See Also

### Reading a document

`init(configuration: Self.ReadConfiguration) throws`

Creates a document and initializes it with the contents of a file.

**Required**

` typealias ReadConfiguration`

The configuration for reading document contents.

Type Alias

# FileDocument.ReadConfiguration

The configuration for reading document contents.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    typealias ReadConfiguration = FileDocumentReadConfiguration

## Discussion

This type is an alias for `FileDocumentReadConfiguration`, which contains a
content type and a file wrapper that you use to access the contents of a
document file. You get a value of this type as an input to the
`init(configuration:)` initializer. Use it to load a document from a file.

## See Also

### Reading a document

`init(configuration: Self.ReadConfiguration) throws`

Creates a document and initializes it with the contents of a file.

**Required**

` static var readableContentTypes: [UTType]`

The file and data types that the document reads from.

**Required**

Instance Method

# fileWrapper(configuration:)

Serializes a document snapshot to a file wrapper.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    func fileWrapper(configuration: Self.WriteConfiguration) throws -> FileWrapper

**Required**

##  Parameters

`configuration`

    

Information about a file that already exists for the document, if any.

## Return Value

The destination to serialize the document contents to. The value can be a
newly created `FileWrapper` or an update of the one provided in the
`configuration` input.

## Discussion

To store a document — for example, in response to a Save command — SwiftUI
calls this method. Use it to serialize the document’s data and create or
modify a file wrapper with the serialized data:

Note

SwiftUI calls this method on a background thread. Don’t make user interface
changes from that thread.

## See Also

### Writing a document

`static var writableContentTypes: [UTType]`

The file types that the document supports saving or exporting to.

**Required** Default implementation provided.

`typealias WriteConfiguration`

The configuration for writing document contents.

Type Property

# writableContentTypes

The file types that the document supports saving or exporting to.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    static var writableContentTypes: [UTType] { get }

**Required** Default implementation provided.

## Discussion

By default, SwiftUI assumes that your document reads and writes the same set
of content types. Only define this property if you need to indicate a
different set of types for writing files. Otherwise, the default
implementation of this property returns the list that you specify in your
implementation of `readableContentTypes`.

## Default Implementations

### FileDocument Implementations

`static var writableContentTypes: [UTType]`

The file types that the document supports saving or exporting to.

## See Also

### Writing a document

`func fileWrapper(configuration: Self.WriteConfiguration) throws ->
FileWrapper`

Serializes a document snapshot to a file wrapper.

**Required**

` typealias WriteConfiguration`

The configuration for writing document contents.

Type Alias

# FileDocument.WriteConfiguration

The configuration for writing document contents.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    typealias WriteConfiguration = FileDocumentWriteConfiguration

## Discussion

This type is an alias for `FileDocumentWriteConfiguration`, which contains a
content type and a file wrapper that you use to access the contents of a
document file, if one already exists. You get a value of this type as an input
to the `fileWrapper(configuration:)` method.

## See Also

### Writing a document

`func fileWrapper(configuration: Self.WriteConfiguration) throws ->
FileWrapper`

Serializes a document snapshot to a file wrapper.

**Required**

` static var writableContentTypes: [UTType]`

The file types that the document supports saving or exporting to.

**Required** Default implementation provided.



# FormStyleConfiguration

Instance Property

# content

A view that is the content of the form.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    let content: FormStyleConfiguration.Content

## See Also

### Getting configuration content

`struct Content`

A type-erased content of a form.

Structure

# FormStyleConfiguration.Content

A type-erased content of a form.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    struct Content

## Relationships

### Conforms To

  * `View`

## See Also

### Getting configuration content

`let content: FormStyleConfiguration.Content`

A view that is the content of the form.



# Font.Weight

Type Property

# black

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static let black: Font.Weight

## See Also

### Getting font weights

`static let bold: Font.Weight`

`static let heavy: Font.Weight`

`static let light: Font.Weight`

`static let medium: Font.Weight`

`static let regular: Font.Weight`

`static let semibold: Font.Weight`

`static let thin: Font.Weight`

`static let ultraLight: Font.Weight`

Type Property

# bold

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static let bold: Font.Weight

## See Also

### Getting font weights

`static let black: Font.Weight`

`static let heavy: Font.Weight`

`static let light: Font.Weight`

`static let medium: Font.Weight`

`static let regular: Font.Weight`

`static let semibold: Font.Weight`

`static let thin: Font.Weight`

`static let ultraLight: Font.Weight`

Type Property

# heavy

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static let heavy: Font.Weight

## See Also

### Getting font weights

`static let black: Font.Weight`

`static let bold: Font.Weight`

`static let light: Font.Weight`

`static let medium: Font.Weight`

`static let regular: Font.Weight`

`static let semibold: Font.Weight`

`static let thin: Font.Weight`

`static let ultraLight: Font.Weight`

Type Property

# light

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static let light: Font.Weight

## See Also

### Getting font weights

`static let black: Font.Weight`

`static let bold: Font.Weight`

`static let heavy: Font.Weight`

`static let medium: Font.Weight`

`static let regular: Font.Weight`

`static let semibold: Font.Weight`

`static let thin: Font.Weight`

`static let ultraLight: Font.Weight`

Type Property

# medium

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static let medium: Font.Weight

## See Also

### Getting font weights

`static let black: Font.Weight`

`static let bold: Font.Weight`

`static let heavy: Font.Weight`

`static let light: Font.Weight`

`static let regular: Font.Weight`

`static let semibold: Font.Weight`

`static let thin: Font.Weight`

`static let ultraLight: Font.Weight`

Type Property

# regular

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static let regular: Font.Weight

## See Also

### Getting font weights

`static let black: Font.Weight`

`static let bold: Font.Weight`

`static let heavy: Font.Weight`

`static let light: Font.Weight`

`static let medium: Font.Weight`

`static let semibold: Font.Weight`

`static let thin: Font.Weight`

`static let ultraLight: Font.Weight`

Type Property

# semibold

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static let semibold: Font.Weight

## See Also

### Getting font weights

`static let black: Font.Weight`

`static let bold: Font.Weight`

`static let heavy: Font.Weight`

`static let light: Font.Weight`

`static let medium: Font.Weight`

`static let regular: Font.Weight`

`static let thin: Font.Weight`

`static let ultraLight: Font.Weight`

Type Property

# thin

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static let thin: Font.Weight

## See Also

### Getting font weights

`static let black: Font.Weight`

`static let bold: Font.Weight`

`static let heavy: Font.Weight`

`static let light: Font.Weight`

`static let medium: Font.Weight`

`static let regular: Font.Weight`

`static let semibold: Font.Weight`

`static let ultraLight: Font.Weight`

Type Property

# ultraLight

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static let ultraLight: Font.Weight

## See Also

### Getting font weights

`static let black: Font.Weight`

`static let bold: Font.Weight`

`static let heavy: Font.Weight`

`static let light: Font.Weight`

`static let medium: Font.Weight`

`static let regular: Font.Weight`

`static let semibold: Font.Weight`

`static let thin: Font.Weight`



# FocusedValue

Initializer

# init(_:)

A new property wrapper for the given object type.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    init(_ objectType: Value.Type) where Value : AnyObject, Value : Observable

##  Parameters

`objectType`

    

The type of object to read the focus value for.

## Discussion

Reads the focused value of the given object type.

Important

This initializer only accepts objects conforming to the `Observable` protocol.
For reading environment objects that conform to `ObservableObject`, use
`FocusedObject`, instead.

To set the focused value that is read by this, use the `focusedValue(_:)` view
modifier.

## See Also

### Creating the value

`init(KeyPath<FocusedValues, Value?>)`

A new property wrapper for the given key path.

Initializer

# init(_:)

A new property wrapper for the given key path.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    init(_ keyPath: KeyPath<FocusedValues, Value?>)

##  Parameters

`keyPath`

    

The key path for the focus value to read.

## Discussion

The value of the property wrapper is updated dynamically as focus changes and
different published values go in and out of scope.

## See Also

### Creating the value

`init(Value.Type)`

A new property wrapper for the given object type.

Instance Property

# wrappedValue

The value for the focus key given the current scope and state of the focused
view hierarchy.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    var wrappedValue: Value? { get }

## Discussion

Returns `nil` when nothing in the focused view hierarchy exports a value.



# ForEach

Initializer

# init(_:content:)

Creates an instance that computes views on demand over a given constant range.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init(
        _ data: Range<Int>,
        @ViewBuilder content: @escaping (Int) -> Content
    )

Available when `Data` is `Range<Int>`, `ID` is `Int`, and `Content` conforms
to `View`.

##  Parameters

`data`

    

A constant range.

`content`

    

The view builder that creates views dynamically.

## Discussion

The instance only reads the initial value of the provided `data` and doesn’t
need to identify views across updates. To compute views on demand over a
dynamic range, use `ForEach/init(_:id:content:)`.

Initializer

# init(_:content:)

Creates an instance that uniquely identifies and creates views across updates
based on the identity of the underlying data.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init(
        _ data: Data,
        @ViewBuilder content: @escaping (Data.Element) -> Content
    )

Available when `Data` conforms to `RandomAccessCollection`, `ID` is
`Data.Element.ID`, `Content` conforms to `View`, and `Data.Element` conforms
to `Identifiable`.

##  Parameters

`data`

    

The identified data that the `ForEach` instance uses to create views
dynamically.

`content`

    

The view builder that creates views dynamically.

## Discussion

It’s important that the `id` of a data element doesn’t change unless you
replace the data element with a new data element that has a new identity. If
the `id` of a data element changes, the content view generated from that data
element loses any current state and animations.

## See Also

### Creating a collection from data

`init<C>(Binding<C>, content: (Binding<C.Element>) -> Content)`

Creates an instance that uniquely identifies and creates views across updates
based on the identity of the underlying data.

Available when `Data` conforms to `RandomAccessCollection`, `ID` conforms to
`Hashable`, and `Content` conforms to `View`.

`init(Data, id: KeyPath<Data.Element, ID>, content: (Data.Element) ->
Content)`

Creates an instance that uniquely identifies and creates views across updates
based on the provided key path to the underlying data’s identifier.

Available when `Data` conforms to `RandomAccessCollection`, `ID` conforms to
`Hashable`, and `Content` conforms to `View`.

`init<C>(Binding<C>, id: KeyPath<C.Element, ID>, content: (Binding<C.Element>)
-> Content)`

Creates an instance that uniquely identifies and creates views across updates
based on the identity of the underlying data.

Available when `Data` conforms to `RandomAccessCollection`, `ID` conforms to
`Hashable`, and `Content` conforms to `View`.

`init(Data)`

Creates an instance that uniquely identifies and creates table rows across
updates based on the identity of the underlying data.

Available when `Data` conforms to `RandomAccessCollection`, `ID` conforms to
`Hashable`, and `Content` conforms to `TableRowContent`.

Initializer

# init(_:content:)

Creates an instance that uniquely identifies and creates views across updates
based on the identity of the underlying data.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init<C>(
        _ data: Binding<C>,
        @ViewBuilder content: @escaping (Binding<C.Element>) -> Content
    ) where Data == LazyMapSequence<C.Indices, (C.Index, ID)>, ID == C.Element.ID, C : MutableCollection, C : RandomAccessCollection, C.Element : Identifiable, C.Index : Hashable

Available when `Data` conforms to `RandomAccessCollection`, `ID` conforms to
`Hashable`, and `Content` conforms to `View`.

##  Parameters

`data`

    

The identified data that the `ForEach` instance uses to create views
dynamically.

`content`

    

The view builder that creates views dynamically.

## Discussion

It’s important that the `id` of a data element doesn’t change unless you
replace the data element with a new data element that has a new identity. If
the `id` of a data element changes, the content view generated from that data
element loses any current state and animations.

## See Also

### Creating a collection from data

`init(Data, content: (Data.Element) -> Content)`

Creates an instance that uniquely identifies and creates views across updates
based on the identity of the underlying data.

Available when `Data` conforms to `RandomAccessCollection`, `ID` is
`Data.Element.ID`, `Content` conforms to `View`, and `Data.Element` conforms
to `Identifiable`.

`init(Data, id: KeyPath<Data.Element, ID>, content: (Data.Element) ->
Content)`

Creates an instance that uniquely identifies and creates views across updates
based on the provided key path to the underlying data’s identifier.

Available when `Data` conforms to `RandomAccessCollection`, `ID` conforms to
`Hashable`, and `Content` conforms to `View`.

`init<C>(Binding<C>, id: KeyPath<C.Element, ID>, content: (Binding<C.Element>)
-> Content)`

Creates an instance that uniquely identifies and creates views across updates
based on the identity of the underlying data.

Available when `Data` conforms to `RandomAccessCollection`, `ID` conforms to
`Hashable`, and `Content` conforms to `View`.

`init(Data)`

Creates an instance that uniquely identifies and creates table rows across
updates based on the identity of the underlying data.

Available when `Data` conforms to `RandomAccessCollection`, `ID` conforms to
`Hashable`, and `Content` conforms to `TableRowContent`.

Initializer

# init(_:id:content:)

Creates an instance that uniquely identifies and creates views across updates
based on the provided key path to the underlying data’s identifier.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init(
        _ data: Data,
        id: KeyPath<Data.Element, ID>,
        @ViewBuilder content: @escaping (Data.Element) -> Content
    )

Available when `Data` conforms to `RandomAccessCollection`, `ID` conforms to
`Hashable`, and `Content` conforms to `View`.

##  Parameters

`data`

    

The data that the `ForEach` instance uses to create views dynamically.

`id`

    

The key path to the provided data’s identifier.

`content`

    

The view builder that creates views dynamically.

## Discussion

It’s important that the `id` of a data element doesn’t change, unless SwiftUI
considers the data element to have been replaced with a new data element that
has a new identity. If the `id` of a data element changes, then the content
view generated from that data element will lose any current state and
animations.

## See Also

### Creating a collection from data

`init(Data, content: (Data.Element) -> Content)`

Creates an instance that uniquely identifies and creates views across updates
based on the identity of the underlying data.

Available when `Data` conforms to `RandomAccessCollection`, `ID` is
`Data.Element.ID`, `Content` conforms to `View`, and `Data.Element` conforms
to `Identifiable`.

`init<C>(Binding<C>, content: (Binding<C.Element>) -> Content)`

Creates an instance that uniquely identifies and creates views across updates
based on the identity of the underlying data.

Available when `Data` conforms to `RandomAccessCollection`, `ID` conforms to
`Hashable`, and `Content` conforms to `View`.

`init<C>(Binding<C>, id: KeyPath<C.Element, ID>, content: (Binding<C.Element>)
-> Content)`

Creates an instance that uniquely identifies and creates views across updates
based on the identity of the underlying data.

Available when `Data` conforms to `RandomAccessCollection`, `ID` conforms to
`Hashable`, and `Content` conforms to `View`.

`init(Data)`

Creates an instance that uniquely identifies and creates table rows across
updates based on the identity of the underlying data.

Available when `Data` conforms to `RandomAccessCollection`, `ID` conforms to
`Hashable`, and `Content` conforms to `TableRowContent`.

Initializer

# init(_:id:content:)

Creates an instance that uniquely identifies and creates views across updates
based on the identity of the underlying data.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init<C>(
        _ data: Binding<C>,
        id: KeyPath<C.Element, ID>,
        @ViewBuilder content: @escaping (Binding<C.Element>) -> Content
    ) where Data == LazyMapSequence<C.Indices, (C.Index, ID)>, C : MutableCollection, C : RandomAccessCollection, C.Index : Hashable

Available when `Data` conforms to `RandomAccessCollection`, `ID` conforms to
`Hashable`, and `Content` conforms to `View`.

##  Parameters

`data`

    

The identified data that the `ForEach` instance uses to create views
dynamically.

`id`

    

The key path to the provided data’s identifier.

`content`

    

The view builder that creates views dynamically.

## Discussion

It’s important that the `id` of a data element doesn’t change unless you
replace the data element with a new data element that has a new identity. If
the `id` of a data element changes, the content view generated from that data
element loses any current state and animations.

## See Also

### Creating a collection from data

`init(Data, content: (Data.Element) -> Content)`

Creates an instance that uniquely identifies and creates views across updates
based on the identity of the underlying data.

Available when `Data` conforms to `RandomAccessCollection`, `ID` is
`Data.Element.ID`, `Content` conforms to `View`, and `Data.Element` conforms
to `Identifiable`.

`init<C>(Binding<C>, content: (Binding<C.Element>) -> Content)`

Creates an instance that uniquely identifies and creates views across updates
based on the identity of the underlying data.

Available when `Data` conforms to `RandomAccessCollection`, `ID` conforms to
`Hashable`, and `Content` conforms to `View`.

`init(Data, id: KeyPath<Data.Element, ID>, content: (Data.Element) ->
Content)`

Creates an instance that uniquely identifies and creates views across updates
based on the provided key path to the underlying data’s identifier.

Available when `Data` conforms to `RandomAccessCollection`, `ID` conforms to
`Hashable`, and `Content` conforms to `View`.

`init(Data)`

Creates an instance that uniquely identifies and creates table rows across
updates based on the identity of the underlying data.

Available when `Data` conforms to `RandomAccessCollection`, `ID` conforms to
`Hashable`, and `Content` conforms to `TableRowContent`.

Initializer

# init(_:)

Creates an instance that uniquely identifies and creates table rows across
updates based on the identity of the underlying data.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    init(_ data: Data) where ID == Data.Element.ID, Content == TableRow<Data.Element>, Data.Element : Identifiable

Available when `Data` conforms to `RandomAccessCollection`, `ID` conforms to
`Hashable`, and `Content` conforms to `TableRowContent`.

##  Parameters

`data`

    

The identified data that the `ForEach` instance uses to create table rows
dynamically.

## Discussion

The following example creates a `Person` type that conforms to `Identifiable`,
and an array of this type called `people`. A `ForEach` instance iterates over
the array, producing new `TableRow` instances implicitly.

## See Also

### Creating a collection from data

`init(Data, content: (Data.Element) -> Content)`

Creates an instance that uniquely identifies and creates views across updates
based on the identity of the underlying data.

Available when `Data` conforms to `RandomAccessCollection`, `ID` is
`Data.Element.ID`, `Content` conforms to `View`, and `Data.Element` conforms
to `Identifiable`.

`init<C>(Binding<C>, content: (Binding<C.Element>) -> Content)`

Creates an instance that uniquely identifies and creates views across updates
based on the identity of the underlying data.

Available when `Data` conforms to `RandomAccessCollection`, `ID` conforms to
`Hashable`, and `Content` conforms to `View`.

`init(Data, id: KeyPath<Data.Element, ID>, content: (Data.Element) ->
Content)`

Creates an instance that uniquely identifies and creates views across updates
based on the provided key path to the underlying data’s identifier.

Available when `Data` conforms to `RandomAccessCollection`, `ID` conforms to
`Hashable`, and `Content` conforms to `View`.

`init<C>(Binding<C>, id: KeyPath<C.Element, ID>, content: (Binding<C.Element>)
-> Content)`

Creates an instance that uniquely identifies and creates views across updates
based on the identity of the underlying data.

Available when `Data` conforms to `RandomAccessCollection`, `ID` conforms to
`Hashable`, and `Content` conforms to `View`.

Initializer

# init(_:content:)

Creates an instance that generates Rotor content by combining, in order,
individual Rotor content for each element in the data given to this `ForEach`.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    init(
        _ data: Data,
        @AccessibilityRotorContentBuilder content: @escaping (Data.Element) -> Content
    )

Available when `Data` conforms to `RandomAccessCollection`, `ID` is
`Data.Element.ID`, `Content` conforms to `AccessibilityRotorContent`, and
`Data.Element` conforms to `Identifiable`.

##  Parameters

`data`

    

The identified data that the `ForEach` instance uses to create views
dynamically.

`content`

    

The result builder that generates Rotor content for each data element.

## Discussion

It’s important that the `id` of a data element doesn’t change unless you
replace the data element with a new data element that has a new identity.

## See Also

### Generating rotor content

`init(Data, id: KeyPath<Data.Element, ID>, content: (Data.Element) ->
Content)`

Creates an instance that generates Rotor content by combining, in order,
individual Rotor content for each element in the data given to this `ForEach`.

Available when `Data` conforms to `RandomAccessCollection`, `ID` conforms to
`Hashable`, and `Content` conforms to `AccessibilityRotorContent`.

Initializer

# init(_:id:content:)

Creates an instance that generates Rotor content by combining, in order,
individual Rotor content for each element in the data given to this `ForEach`.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    init(
        _ data: Data,
        id: KeyPath<Data.Element, ID>,
        @AccessibilityRotorContentBuilder content: @escaping (Data.Element) -> Content
    )

Available when `Data` conforms to `RandomAccessCollection`, `ID` conforms to
`Hashable`, and `Content` conforms to `AccessibilityRotorContent`.

##  Parameters

`data`

    

The data that the `ForEach` instance uses to create views dynamically.

`id`

    

The key path to the provided data’s identifier.

`content`

    

The result builder that generates Rotor content for each data element.

## Discussion

It’s important that the `id` of a data element doesn’t change, unless SwiftUI
considers the data element to have been replaced with a new data element that
has a new identity.

## See Also

### Generating rotor content

`init(Data, content: (Data.Element) -> Content)`

Creates an instance that generates Rotor content by combining, in order,
individual Rotor content for each element in the data given to this `ForEach`.

Available when `Data` conforms to `RandomAccessCollection`, `ID` is
`Data.Element.ID`, `Content` conforms to `AccessibilityRotorContent`, and
`Data.Element` conforms to `Identifiable`.

Initializer

# init(_:content:)

Creates an instance that computes table rows on demand over a given constant
range.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    init<V>(
        _ data: Range<Int>,
        @TableRowBuilder<V> content: @escaping (Int) -> Content
    ) where Data == Range<Int>, ID == Int, V == Content.TableRowValue

Available when `Data` conforms to `RandomAccessCollection`, `ID` conforms to
`Hashable`, and `Content` conforms to `TableRowContent`.

##  Parameters

`data`

    

A constant range.

`content`

    

The table row builder that creates rows dynamically.

## Discussion

The instance only reads the initial value of the provided `data` and doesn’t
need to identify rows across updates. To compute rows on demand over a dynamic
range, use `ForEach/init(_:id:content:)`.

## See Also

### Creating a collection of table rows

`init<V>(Data, content: (Data.Element) -> Content)`

Creates an instance that uniquely identifies and creates table rows across
updates based on the identity of the underlying data.

Available when `Data` conforms to `RandomAccessCollection`, `ID` conforms to
`Hashable`, and `Content` conforms to `TableRowContent`.

`init<V>(Data, id: KeyPath<Data.Element, ID>, content: (Data.Element) ->
Content)`

Creates an instance that uniquely identifies and creates table rows across
updates based on the provided key path to the underlying data’s identifier.

Available when `Data` conforms to `RandomAccessCollection`, `ID` conforms to
`Hashable`, and `Content` conforms to `TableRowContent`.

Initializer

# init(_:content:)

Creates an instance that uniquely identifies and creates table rows across
updates based on the identity of the underlying data.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    init<V>(
        _ data: Data,
        @TableRowBuilder<V> content: @escaping (Data.Element) -> Content
    ) where ID == Data.Element.ID, V == Content.TableRowValue, Data.Element : Identifiable

Available when `Data` conforms to `RandomAccessCollection`, `ID` conforms to
`Hashable`, and `Content` conforms to `TableRowContent`.

##  Parameters

`data`

    

The identified data that the `ForEach` instance uses to create table rows
dynamically.

`content`

    

The table row builder that creates rows dynamically.

## See Also

### Creating a collection of table rows

`init<V>(Range<Int>, content: (Int) -> Content)`

Creates an instance that computes table rows on demand over a given constant
range.

Available when `Data` conforms to `RandomAccessCollection`, `ID` conforms to
`Hashable`, and `Content` conforms to `TableRowContent`.

`init<V>(Data, id: KeyPath<Data.Element, ID>, content: (Data.Element) ->
Content)`

Creates an instance that uniquely identifies and creates table rows across
updates based on the provided key path to the underlying data’s identifier.

Available when `Data` conforms to `RandomAccessCollection`, `ID` conforms to
`Hashable`, and `Content` conforms to `TableRowContent`.

Initializer

# init(_:id:content:)

Creates an instance that uniquely identifies and creates table rows across
updates based on the provided key path to the underlying data’s identifier.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    init<V>(
        _ data: Data,
        id: KeyPath<Data.Element, ID>,
        @TableRowBuilder<V> content: @escaping (Data.Element) -> Content
    ) where V == Content.TableRowValue

Available when `Data` conforms to `RandomAccessCollection`, `ID` conforms to
`Hashable`, and `Content` conforms to `TableRowContent`.

##  Parameters

`data`

    

The data that the `ForEach` instance uses to create table rows dynamically.

`id`

    

The key path to the provided data’s identifier.

`content`

    

The table row builder that creates rows dynamically.

## See Also

### Creating a collection of table rows

`init<V>(Range<Int>, content: (Int) -> Content)`

Creates an instance that computes table rows on demand over a given constant
range.

Available when `Data` conforms to `RandomAccessCollection`, `ID` conforms to
`Hashable`, and `Content` conforms to `TableRowContent`.

`init<V>(Data, content: (Data.Element) -> Content)`

Creates an instance that uniquely identifies and creates table rows across
updates based on the identity of the underlying data.

Available when `Data` conforms to `RandomAccessCollection`, `ID` conforms to
`Hashable`, and `Content` conforms to `TableRowContent`.

Initializer

# init(_:content:)

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    init(
        _ data: Data,
        @ChartContentBuilder content: @escaping (Data.Element) -> Content
    )

Available when `Data` conforms to `RandomAccessCollection`, `ID` is
`Data.Element.ID`, `Content` conforms to `ChartContent`, and `Data.Element`
conforms to `Identifiable`.

## See Also

### Creating chart content

`init(Data, id: KeyPath<Data.Element, ID>, content: (Data.Element) ->
Content)`

Available when `Data` conforms to `RandomAccessCollection`, `ID` conforms to
`Hashable`, and `Content` conforms to `ChartContent`.

Initializer

# init(_:id:content:)

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    init(
        _ data: Data,
        id: KeyPath<Data.Element, ID>,
        @ChartContentBuilder content: @escaping (Data.Element) -> Content
    )

Available when `Data` conforms to `RandomAccessCollection`, `ID` conforms to
`Hashable`, and `Content` conforms to `ChartContent`.

## See Also

### Creating chart content

`init(Data, content: (Data.Element) -> Content)`

Available when `Data` conforms to `RandomAccessCollection`, `ID` is
`Data.Element.ID`, `Content` conforms to `ChartContent`, and `Data.Element`
conforms to `Identifiable`.

Initializer

# init(_:editActions:content:)

Creates an instance that uniquely identifies and creates views across updates
based on the identity of the underlying data.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    init<C, R>(
        _ data: Binding<C>,
        editActions: EditActions<C>,
        @ViewBuilder content: @escaping (Binding<C.Element>) -> R
    ) where Data == IndexedIdentifierCollection<C, ID>, ID == C.Element.ID, Content == EditableCollectionContent<R, C>, C : MutableCollection, C : RandomAccessCollection, R : View, C.Element : Identifiable, C.Index : Hashable

Available when `Data` conforms to `RandomAccessCollection` and `ID` conforms
to `Hashable`.

##  Parameters

`data`

    

The identified data that the `ForEach` instance uses to create views
dynamically and can be edited by the user.

`editActions`

    

The edit actions that are synthesized on `data`.

`content`

    

The view builder that creates views dynamically.

## Discussion

It’s important that the `id` of a data element doesn’t change unless you
replace the data element with a new data element that has a new identity. If
the `id` of a data element changes, the content view generated from that data
element loses any current state and animations.

When placed inside a `List` the edit actions (like delete or move) can be
automatically synthesized by specifying an appropriate `EditActions`.

The following example shows a list of recipes whose elements can be deleted
and reordered:

Use `deleteDisabled(_:)` and `moveDisabled(_:)` to disable respectively delete
or move actions on a per-row basis.

The following example shows a list of recipes whose elements can be deleted
only if they satisfy a condition:

Explicit `DynamicViewContent.onDelete(perform:)`,
`DynamicViewContent.onMove(perform:)`, or
`View.swipeActions(edge:allowsFullSwipe:content:)` modifiers will override any
synthesized actions. Use this modifier if you need fine-grain control on how
mutations are applied to the data driving the `ForEach`. For example, if you
need to execute side effects or call into your existing model code.

## See Also

### Creating editable content

`init<C, R>(Binding<C>, id: KeyPath<C.Element, ID>, editActions:
EditActions<C>, content: (Binding<C.Element>) -> R)`

Creates an instance that uniquely identifies and creates views across updates
based on the identity of the underlying data.

Available when `Data` conforms to `RandomAccessCollection` and `ID` conforms
to `Hashable`.

Initializer

# init(_:id:editActions:content:)

Creates an instance that uniquely identifies and creates views across updates
based on the identity of the underlying data.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    init<C, R>(
        _ data: Binding<C>,
        id: KeyPath<C.Element, ID>,
        editActions: EditActions<C>,
        @ViewBuilder content: @escaping (Binding<C.Element>) -> R
    ) where Data == IndexedIdentifierCollection<C, ID>, Content == EditableCollectionContent<R, C>, C : MutableCollection, C : RandomAccessCollection, R : View, C.Index : Hashable

Available when `Data` conforms to `RandomAccessCollection` and `ID` conforms
to `Hashable`.

##  Parameters

`data`

    

The identified data that the `ForEach` instance uses to create views
dynamically and can be edited by the user.

`id`

    

The key path to the provided data’s identifier.

`editActions`

    

The edit actions that are synthesized on `data`.

`content`

    

The view builder that creates views dynamically.

## Discussion

It’s important that the `id` of a data element doesn’t change unless you
replace the data element with a new data element that has a new identity. If
the `id` of a data element changes, the content view generated from that data
element loses any current state and animations.

When placed inside a `List` the edit actions (like delete or move) can be
automatically synthesized by specifying an appropriate `EditActions`.

The following example shows a list of recipes whose elements can be deleted
and reordered:

Use `deleteDisabled(_:)` and `moveDisabled(_:)` to disable respectively delete
or move actions on a per-row basis.

The following example shows a list of recipes whose elements can be deleted
only if they satisfy a condition:

Explicit `DynamicViewContent.onDelete(perform:)`,
`DynamicViewContent.onMove(perform:)`, or
`View.swipeActions(edge:allowsFullSwipe:content:)` modifiers will override any
synthesized actions. Use this modifier if you need fine-grain control on how
mutations are applied to the data driving the `ForEach`. For example, if you
need to execute side effects or call into your existing model code.

## See Also

### Creating editable content

`init<C, R>(Binding<C>, editActions: EditActions<C>, content:
(Binding<C.Element>) -> R)`

Creates an instance that uniquely identifies and creates views across updates
based on the identity of the underlying data.

Available when `Data` conforms to `RandomAccessCollection` and `ID` conforms
to `Hashable`.

Initializer

# init(_:content:)

RealityKit  SwiftUI  visionOS 1.0+

    
    
    init(
        _ data: Data,
        @AttachmentContentBuilder content: @escaping (Data.Element) -> Content
    )

Available when `Data` conforms to `RandomAccessCollection`, `ID` is
`Data.Element.ID`, `Content` conforms to `AttachmentContent`, and
`Data.Element` conforms to `Identifiable`.

## See Also

### Creating attachment content

`init(Data, id: KeyPath<Data.Element, ID>, content: (Data.Element) ->
Content)`

Available when `Data` conforms to `RandomAccessCollection`, `ID` conforms to
`Hashable`, and `Content` conforms to `AttachmentContent`.

Initializer

# init(_:id:content:)

RealityKit  SwiftUI  visionOS 1.0+

    
    
    init(
        _ data: Data,
        id: KeyPath<Data.Element, ID>,
        @AttachmentContentBuilder content: @escaping (Data.Element) -> Content
    )

Available when `Data` conforms to `RandomAccessCollection`, `ID` conforms to
`Hashable`, and `Content` conforms to `AttachmentContent`.

## See Also

### Creating attachment content

`init(Data, content: (Data.Element) -> Content)`

Available when `Data` conforms to `RandomAccessCollection`, `ID` is
`Data.Element.ID`, `Content` conforms to `AttachmentContent`, and
`Data.Element` conforms to `Identifiable`.

Instance Property

# content

A function to create content on demand using the underlying data.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var content: (Data.Element) -> Content

## See Also

### Accessing content

`var data: Data`

The collection of underlying identified data that SwiftUI uses to create views
dynamically.

Instance Property

# data

The collection of underlying identified data that SwiftUI uses to create views
dynamically.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var data: Data

## See Also

### Accessing content

`var content: (Data.Element) -> Content`

A function to create content on demand using the underlying data.

Initializer

# init(_:content:)

Creates an instance that computes map content on demand over a given constant
range.

MapKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  tvOS 17.0+  watchOS
10.0+

    
    
    init(
        _ data: Range<Int>,
        @MapContentBuilder content: @escaping (Int) -> Content
    ) where Data == Range<Int>, ID == Int

Available when `Data` conforms to `RandomAccessCollection`, `ID` conforms to
`Hashable`, and `Content` conforms to `MapContent`.

##  Parameters

`data`

    

A constant range.

`content`

    

The map content builder that creates map content dynamically.

## Discussion

The instance only reads the initial value of the provided `data` and doesn’t
need to identify map content across updates. To compute map map content on
demand over a dynamic range, use `ForEach/init(_:id:content:)`.

Initializer

# init(_:content:)

Creates an instance that uniquely identifies and creates map content across
updates based on the identity of the underlying data.

MapKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  tvOS 17.0+  watchOS
10.0+

    
    
    init(
        _ data: Data,
        @MapContentBuilder content: @escaping (Data.Element) -> Content
    ) where ID == Data.Element.ID, Data.Element : Identifiable

Available when `Data` conforms to `RandomAccessCollection`, `ID` conforms to
`Hashable`, and `Content` conforms to `MapContent`.

##  Parameters

`data`

    

The identified data that the `ForEach` instance uses to create map content
dynamically.

`content`

    

The map content builder that creates map content dynamically.

## Discussion

It’s important that the `id` of a data element doesn’t change unless you
replace the data element with a new data element that has a new identity. If
the `id` of a data element changes, the content view generated from that data
element loses any current state and animations.

Initializer

# init(_:id:content:)

Creates an instance that uniquely identifies and creates map content across
updates based on the provided key path to the underlying data’s identifier.

MapKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  tvOS 17.0+  watchOS
10.0+

    
    
    init(
        _ data: Data,
        id: KeyPath<Data.Element, ID>,
        @MapContentBuilder content: @escaping (Data.Element) -> Content
    )

Available when `Data` conforms to `RandomAccessCollection`, `ID` conforms to
`Hashable`, and `Content` conforms to `MapContent`.

##  Parameters

`data`

    

The data that the `ForEach` instance uses to create map content dynamically.

`id`

    

The key path to the provided data’s identifier.

`content`

    

The map content builder that creates map content dynamically.

## Discussion

It’s important that the `id` of a data element doesn’t change, unless the data
element has been replaced with a new data element that has a new identity. If
the `id` of a data element changes, then the map content generated from that
data element will lose any current state and animations.

Type Alias

# ForEach.Body

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    typealias Body = Never

Available when `Data` conforms to `RandomAccessCollection`, `ID` conforms to
`Hashable`, and `Content` conforms to `View`.

Collection

API Collection

# AttachmentContent Implementations

## Topics

### Instance Properties

`var body: Never`

Available when `Data` conforms to `RandomAccessCollection`, `ID` conforms to
`Hashable`, and `Content` conforms to `AttachmentContent`.

### Type Aliases

`typealias Body`

Available when `Data` conforms to `RandomAccessCollection`, `ID` conforms to
`Hashable`, and `Content` conforms to `AttachmentContent`.

Collection

API Collection

# MapContent Implementations

## Topics

### Instance Methods

`func annotationSubtitles(Visibility) -> some MapContent`

Sets the visibility of subtitles for markers and annotations.

`func annotationTitles(Visibility) -> some MapContent`

Sets the visibility of titles for markers and annotations.

`func foregroundStyle(some ShapeStyle) -> some MapContent`

Specifies the shape style used to fill content in drawing map overlays.

`func mapOverlayLevel(level: MKOverlayLevel) -> some MapContent`

Specifies the position of overlays relative to other map content.

`func stroke(some ShapeStyle, lineWidth: CGFloat) -> some MapContent`

Applies the given shape style to drawn map overlays.

`func stroke(some ShapeStyle, style: StrokeStyle) -> some MapContent`

Applies the given shape style to drawn map overlays.

`func stroke(lineWidth: CGFloat) -> some MapContent`

Sets the line width used for drawing map overlays.

`func strokeStyle(style: StrokeStyle) -> some MapContent`

Applies the given stroke style to drawn map overlays.

`func tag<V>(V) -> some MapContent`

Sets the unique tag value of this piece of map content.

`func tint<S>(S) -> some MapContent`

The tint shape style to apply to map content.

### Type Aliases

`typealias Body`

Available when `Data` conforms to `RandomAccessCollection`, `ID` conforms to
`Hashable`, and `Content` conforms to `MapContent`.



# Form

Initializer

# init(content:)

Creates a form with the provided content.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init(@ViewBuilder content: () -> Content)

##  Parameters

`content`

    

A `ViewBuilder` that provides the content for the form.

Initializer

# init(_:)

Creates a form based on a form style configuration.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    init(_ configuration: FormStyleConfiguration)

Available when `Content` is `FormStyleConfiguration.Content`.

##  Parameters

`configuration`

    

The properties of the form.



# FocusedBinding

Initializer

# init(_:)

A new property wrapper for the given key path.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    init(_ keyPath: KeyPath<FocusedValues, Binding<Value>?>)

##  Parameters

`keyPath`

    

The key path for the focus value to read.

## Discussion

The value of the property wrapper is updated dynamically as focus changes and
different published bindings go in and out of scope.

Instance Property

# projectedValue

A binding to the optional value.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    var projectedValue: Binding<Value?> { get }

## Discussion

The unwrapped value is `nil` when no focused view hierarchy has published a
corresponding binding.

## See Also

### Getting the value

`var wrappedValue: Value?`

The unwrapped value for the focus key given the current scope and state of the
focused view hierarchy.

Instance Property

# wrappedValue

The unwrapped value for the focus key given the current scope and state of the
focused view hierarchy.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    var wrappedValue: Value? { get nonmutating set }

## See Also

### Getting the value

`var projectedValue: Binding<Value?>`

A binding to the optional value.



# Font.Design

Case

# Font.Design.default

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    case `default`

## See Also

### Getting font designs

`case monospaced`

`case rounded`

`case serif`

Case

# Font.Design.monospaced

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
7.0+  visionOS 1.0+

    
    
    case monospaced

## See Also

### Getting font designs

`case `default``

`case rounded`

`case serif`

Case

# Font.Design.rounded

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    case rounded

## See Also

### Getting font designs

`case `default``

`case monospaced`

`case serif`

Case

# Font.Design.serif

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
7.0+  visionOS 1.0+

    
    
    case serif

## See Also

### Getting font designs

`case `default``

`case monospaced`

`case rounded`



# FocusInteractions

Type Property

# automatic

The view supports whatever focus-driven interactions are commonly expected for
interactive content on the current platform.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    static var automatic: FocusInteractions { get }

## See Also

### Creating the interaction types

`static let activate: FocusInteractions`

The view has a primary action that can be activated via focus gestures.

`static let edit: FocusInteractions`

The view captures input from non-spatial sources like a keyboard or Digital
Crown.

Type Property

# activate

The view has a primary action that can be activated via focus gestures.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    static let activate: FocusInteractions

## Discussion

On macOS and iOS, focus-driven activation interactions are only possible when
all-controls keyboard navigation is enabled. On tvOS and watchOS, focus-driven
activation interactions are always possible.

## See Also

### Creating the interaction types

`static var automatic: FocusInteractions`

The view supports whatever focus-driven interactions are commonly expected for
interactive content on the current platform.

`static let edit: FocusInteractions`

The view captures input from non-spatial sources like a keyboard or Digital
Crown.

Type Property

# edit

The view captures input from non-spatial sources like a keyboard or Digital
Crown.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    static let edit: FocusInteractions

## Discussion

Views that support focus-driven editing interactions become focused when the
user taps or clicks on them, or when the user issues a focus movement command.

## See Also

### Creating the interaction types

`static var automatic: FocusInteractions`

The view supports whatever focus-driven interactions are commonly expected for
interactive content on the current platform.

`static let activate: FocusInteractions`

The view has a primary action that can be activated via focus gestures.



# FetchedResults

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



# FillStyle

Initializer

# init(eoFill:antialiased:)

Creates a new fill style with the specified settings.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init(
        eoFill: Bool = false,
        antialiased: Bool = true
    )

##  Parameters

`eoFill`

    

A Boolean value that indicates whether to use the even-odd rule for rendering
a shape. Pass `false` to use the non-zero winding number rule instead.

`antialiased`

    

A Boolean value that indicates whether to use antialiasing when rendering the
edges of a shape.

Instance Property

# isEOFilled

A Boolean value that indicates whether to use the even-odd rule when rendering
a shape.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var isEOFilled: Bool

## Discussion

When `isOEFilled` is `false`, the style uses the non-zero winding number rule.

## See Also

### Setting fill style properties

`var isAntialiased: Bool`

A Boolean value that indicates whether to apply antialiasing to the edges of a
shape.

Instance Property

# isAntialiased

A Boolean value that indicates whether to apply antialiasing to the edges of a
shape.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var isAntialiased: Bool

## See Also

### Setting fill style properties

`var isEOFilled: Bool`

A Boolean value that indicates whether to use the even-odd rule when rendering
a shape.



# FillShapeView

Initializer

# init(shape:style:fillStyle:background:)

Create a FillShapeView.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    init(
        shape: Content,
        style: Style,
        fillStyle: FillStyle,
        background: Background
    )

Instance Property

# background

The background shown beneath this view.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    var background: Background { get set }

## See Also

### Getting shape view properties

`var fillStyle: FillStyle`

The fill style used when filling this view’s shape.

`var shape: Content`

The shape that this type draws and provides for other drawing operations.

`var style: Style`

The style that fills this view’s shape.

Instance Property

# fillStyle

The fill style used when filling this view’s shape.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    var fillStyle: FillStyle { get set }

## See Also

### Getting shape view properties

`var background: Background`

The background shown beneath this view.

`var shape: Content`

The shape that this type draws and provides for other drawing operations.

`var style: Style`

The style that fills this view’s shape.

Instance Property

# shape

The shape that this type draws and provides for other drawing operations.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    var shape: Content { get set }

## See Also

### Getting shape view properties

`var background: Background`

The background shown beneath this view.

`var fillStyle: FillStyle`

The fill style used when filling this view’s shape.

`var style: Style`

The style that fills this view’s shape.

Instance Property

# style

The style that fills this view’s shape.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    var style: Style { get set }

## See Also

### Getting shape view properties

`var background: Background`

The background shown beneath this view.

`var fillStyle: FillStyle`

The fill style used when filling this view’s shape.

`var shape: Content`

The shape that this type draws and provides for other drawing operations.



# Font.Width

Type Property

# compressed

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    static let compressed: Font.Width

## See Also

### Getting standard font widths

`static let condensed: Font.Width`

`static let expanded: Font.Width`

`static let standard: Font.Width`

Type Property

# condensed

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    static let condensed: Font.Width

## See Also

### Getting standard font widths

`static let compressed: Font.Width`

`static let expanded: Font.Width`

`static let standard: Font.Width`

Type Property

# expanded

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    static let expanded: Font.Width

## See Also

### Getting standard font widths

`static let compressed: Font.Width`

`static let condensed: Font.Width`

`static let standard: Font.Width`

Type Property

# standard

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    static let standard: Font.Width

## See Also

### Getting standard font widths

`static let compressed: Font.Width`

`static let condensed: Font.Width`

`static let expanded: Font.Width`

Initializer

# init(_:)

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    init(_ value: CGFloat)

Instance Property

# value

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    var value: CGFloat



# Focus

Instance Method

# focusable(_:)

Specifies if the view is focusable.

iOS 17.0+  iPadOS 17.0+  macOS 12.0+  Mac Catalyst 17.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func focusable(_ isFocusable: Bool = true) -> some View
    

##  Parameters

`isFocusable`

    

A Boolean value that indicates whether this view is focusable.

## Return Value

A view that sets whether a view is focusable.

## See Also

### Indicating that a view can receive focus

`func focusable(Bool, interactions: FocusInteractions) -> some View`

Specifies if the view is focusable, and if so, what focus-driven interactions
it supports.

`struct FocusInteractions`

Values describe different focus interactions that a view can support.

Instance Method

# focusable(_:interactions:)

Specifies if the view is focusable, and if so, what focus-driven interactions
it supports.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func focusable(
        _ isFocusable: Bool = true,
        interactions: FocusInteractions
    ) -> some View
    

##  Parameters

`isFocusable`

    

`true` if the view should participate in focus; `false` otherwise. The default
value is `true`.

`interactions`

    

The types of focus interactions supported by the view. The default value is
`.automatic`.

## Return Value

A view that sets whether its child is focusable.

## Discussion

By default, SwiftUI enables all possible focus interactions. However, on macOS
and iOS it is conventional for button-like views to only accept focus when the
user has enabled keyboard navigation system-wide in the Settings app. Clients
can reproduce this behavior with custom views by only supporting `.activate`
interactions.

Note

The focus interactions allowed for custom views changed in macOS
14—previously, custom views could only become focused with keyboard navigation
enabled system-wide. Clients built using older SDKs will continue to see the
older focus behavior, while custom views in clients built using macOS 14 or
later will always be focusable unless the client requests otherwise by
specifying a restricted set of focus interactions.

## See Also

### Indicating that a view can receive focus

`func focusable(Bool) -> some View`

Specifies if the view is focusable.

`struct FocusInteractions`

Values describe different focus interactions that a view can support.

Structure

# FocusInteractions

Values describe different focus interactions that a view can support.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    struct FocusInteractions

## Topics

### Creating the interaction types

`static var automatic: FocusInteractions`

The view supports whatever focus-driven interactions are commonly expected for
interactive content on the current platform.

`static let activate: FocusInteractions`

The view has a primary action that can be activated via focus gestures.

`static let edit: FocusInteractions`

The view captures input from non-spatial sources like a keyboard or Digital
Crown.

## Relationships

### Conforms To

  * `Equatable`
  * `ExpressibleByArrayLiteral`
  * `OptionSet`
  * `RawRepresentable`
  * `Sendable`
  * `SetAlgebra`

## See Also

### Indicating that a view can receive focus

`func focusable(Bool) -> some View`

Specifies if the view is focusable.

`func focusable(Bool, interactions: FocusInteractions) -> some View`

Specifies if the view is focusable, and if so, what focus-driven interactions
it supports.

Instance Method

# focused(_:equals:)

Modifies this view by binding its focus state to the given state value.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func focused<Value>(
        _ binding: FocusState<Value>.Binding,
        equals value: Value
    ) -> some View where Value : Hashable
    

##  Parameters

`binding`

    

The state binding to register. When focus moves to the modified view, the
binding sets the bound value to the corresponding match value. If a caller
sets the state value programmatically to the matching value, then focus moves
to the modified view. When focus leaves the modified view, the binding sets
the bound value to `nil`. If a caller sets the value to `nil`, SwiftUI
automatically dismisses focus.

`value`

    

The value to match against when determining whether the binding should change.

## Return Value

The modified view.

## Discussion

Use this modifier to cause the view to receive focus whenever the the
`binding` equals the `value`. Typically, you create an enumeration of fields
that may receive focus, bind an instance of this enumeration, and assign its
cases to focusable views.

The following example uses the cases of a `LoginForm` enumeration to bind the
focus state of two `TextField` views. A sign-in button validates the fields
and sets the bound `focusedField` value to any field that requires the user to
correct a problem.

To control focus using a Boolean, use the `focused(_:)` method instead.

## See Also

### Managing focus state

`func focused(FocusState<Bool>.Binding) -> some View`

Modifies this view by binding its focus state to the given Boolean state
value.

`var isFocused: Bool`

Returns whether the nearest focusable ancestor has focus.

`struct FocusState`

A property wrapper type that can read and write a value that SwiftUI updates
as the placement of focus within the scene changes.

`struct FocusedValue`

A property wrapper for observing values from the focused view or one of its
ancestors.

`protocol FocusedValueKey`

A protocol for identifier types used when publishing and observing focused
values.

`struct FocusedBinding`

A convenience property wrapper for observing and automatically unwrapping
state bindings from the focused view or one of its ancestors.

Instance Method

# focused(_:)

Modifies this view by binding its focus state to the given Boolean state
value.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func focused(_ condition: FocusState<Bool>.Binding) -> some View
    

##  Parameters

`condition`

    

The focus state to bind. When focus moves to the view, the binding sets the
bound value to `true`. If a caller sets the value to `true` programmatically,
then focus moves to the modified view. When focus leaves the modified view,
the binding sets the value to `false`. If a caller sets the value to `false`,
SwiftUI automatically dismisses focus.

## Return Value

The modified view.

## Discussion

Use this modifier to cause the view to receive focus whenever the the
`condition` value is `true`. You can use this modifier to observe the focus
state of a single view, or programmatically set and remove focus from the
view.

In the following example, a single `TextField` accepts a user’s desired
`username`. The text field binds its focus state to the Boolean value
`usernameFieldIsFocused`. A “Submit” button’s action verifies whether the name
is available. If the name is unavailable, the button sets
`usernameFieldIsFocused` to `true`, which causes focus to return to the text
field, so the user can enter a different name.

To control focus by matching a value, use the `focused(_:equals:)` method
instead.

## See Also

### Managing focus state

`func focused<Value>(FocusState<Value>.Binding, equals: Value) -> some View`

Modifies this view by binding its focus state to the given state value.

`var isFocused: Bool`

Returns whether the nearest focusable ancestor has focus.

`struct FocusState`

A property wrapper type that can read and write a value that SwiftUI updates
as the placement of focus within the scene changes.

`struct FocusedValue`

A property wrapper for observing values from the focused view or one of its
ancestors.

`protocol FocusedValueKey`

A protocol for identifier types used when publishing and observing focused
values.

`struct FocusedBinding`

A convenience property wrapper for observing and automatically unwrapping
state bindings from the focused view or one of its ancestors.

Instance Property

# isFocused

Returns whether the nearest focusable ancestor has focus.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    var isFocused: Bool { get }

## Discussion

If there is no focusable ancestor, the value is `false`.

## See Also

### Managing focus state

`func focused<Value>(FocusState<Value>.Binding, equals: Value) -> some View`

Modifies this view by binding its focus state to the given state value.

`func focused(FocusState<Bool>.Binding) -> some View`

Modifies this view by binding its focus state to the given Boolean state
value.

`struct FocusState`

A property wrapper type that can read and write a value that SwiftUI updates
as the placement of focus within the scene changes.

`struct FocusedValue`

A property wrapper for observing values from the focused view or one of its
ancestors.

`protocol FocusedValueKey`

A protocol for identifier types used when publishing and observing focused
values.

`struct FocusedBinding`

A convenience property wrapper for observing and automatically unwrapping
state bindings from the focused view or one of its ancestors.

Structure

# FocusState

A property wrapper type that can read and write a value that SwiftUI updates
as the placement of focus within the scene changes.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    @frozen @propertyWrapper
    struct FocusState<Value> where Value : Hashable

## Overview

Use this property wrapper in conjunction with `focused(_:equals:)` and
`focused(_:)` to describe views whose appearance and contents relate to the
location of focus in the scene. When focus enters the modified view, the
wrapped value of this property updates to match a given prototype value.
Similarly, when focus leaves, the wrapped value of this property resets to
`nil` or `false`. Setting the property’s value programmatically has the
reverse effect, causing focus to move to the view associated with the updated
value.

In the following example of a simple login screen, when the user presses the
Sign In button and one of the fields is still empty, focus moves to that
field. Otherwise, the sign-in process proceeds.

To allow for cases where focus is completely absent from a view tree, the
wrapped value must be either an optional or a Boolean. Set the focus binding
to `false` or `nil` as appropriate to remove focus from all bound fields. You
can also use this to remove focus from a `TextField` and thereby dismiss the
keyboard.

### Avoid ambiguous focus bindings

The same view can have multiple focus bindings. In the following example,
setting `focusedField` to either `name` or `fullName` causes the field to
receive focus:

On the other hand, binding the same value to two views is ambiguous. In the
following example, two separate fields bind focus to the `name` value:

If the user moves focus to either field, the `focusedField` binding updates to
`name`. However, if the app programmatically sets the value to `name`, SwiftUI
chooses the first candidate, which in this case is the “Name” field. SwiftUI
also emits a runtime warning in this case, since the repeated binding is
likely a programmer error.

## Topics

### Creating a focus state

`init<T>()`

Creates a focus state that binds to an optional type.

`init()`

Creates a focus state that binds to a Boolean.

### Inspecting the focus state

`var projectedValue: FocusState<Value>.Binding`

A projection of the focus state value that returns a binding.

`struct Binding`

A property wrapper type that can read and write a value that indicates the
current focus location.

`var wrappedValue: Value`

The current state value, taking into account whatever bindings might be in
effect due to the current location of focus.

## Relationships

### Conforms To

  * `DynamicProperty`

## See Also

### Managing focus state

`func focused<Value>(FocusState<Value>.Binding, equals: Value) -> some View`

Modifies this view by binding its focus state to the given state value.

`func focused(FocusState<Bool>.Binding) -> some View`

Modifies this view by binding its focus state to the given Boolean state
value.

`var isFocused: Bool`

Returns whether the nearest focusable ancestor has focus.

`struct FocusedValue`

A property wrapper for observing values from the focused view or one of its
ancestors.

`protocol FocusedValueKey`

A protocol for identifier types used when publishing and observing focused
values.

`struct FocusedBinding`

A convenience property wrapper for observing and automatically unwrapping
state bindings from the focused view or one of its ancestors.

Structure

# FocusedValue

A property wrapper for observing values from the focused view or one of its
ancestors.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    @propertyWrapper
    struct FocusedValue<Value>

## Overview

If multiple views publish values using the same key, the wrapped property will
reflect the value from the view closest to focus.

## Topics

### Creating the value

`init(Value.Type)`

A new property wrapper for the given object type.

`init(KeyPath<FocusedValues, Value?>)`

A new property wrapper for the given key path.

### Getting the value

`var wrappedValue: Value?`

The value for the focus key given the current scope and state of the focused
view hierarchy.

## Relationships

### Conforms To

  * `DynamicProperty`

## See Also

### Managing focus state

`func focused<Value>(FocusState<Value>.Binding, equals: Value) -> some View`

Modifies this view by binding its focus state to the given state value.

`func focused(FocusState<Bool>.Binding) -> some View`

Modifies this view by binding its focus state to the given Boolean state
value.

`var isFocused: Bool`

Returns whether the nearest focusable ancestor has focus.

`struct FocusState`

A property wrapper type that can read and write a value that SwiftUI updates
as the placement of focus within the scene changes.

`protocol FocusedValueKey`

A protocol for identifier types used when publishing and observing focused
values.

`struct FocusedBinding`

A convenience property wrapper for observing and automatically unwrapping
state bindings from the focused view or one of its ancestors.

Protocol

# FocusedValueKey

A protocol for identifier types used when publishing and observing focused
values.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    protocol FocusedValueKey

## Overview

Unlike `EnvironmentKey`, `FocusedValueKey` has no default value requirement,
because the default value for a key is always `nil`.

## Topics

### Specifying the value type

`associatedtype Value`

**Required**

## See Also

### Managing focus state

`func focused<Value>(FocusState<Value>.Binding, equals: Value) -> some View`

Modifies this view by binding its focus state to the given state value.

`func focused(FocusState<Bool>.Binding) -> some View`

Modifies this view by binding its focus state to the given Boolean state
value.

`var isFocused: Bool`

Returns whether the nearest focusable ancestor has focus.

`struct FocusState`

A property wrapper type that can read and write a value that SwiftUI updates
as the placement of focus within the scene changes.

`struct FocusedValue`

A property wrapper for observing values from the focused view or one of its
ancestors.

`struct FocusedBinding`

A convenience property wrapper for observing and automatically unwrapping
state bindings from the focused view or one of its ancestors.

Structure

# FocusedBinding

A convenience property wrapper for observing and automatically unwrapping
state bindings from the focused view or one of its ancestors.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    @propertyWrapper
    struct FocusedBinding<Value>

## Overview

If multiple views publish bindings using the same key, the wrapped property
will reflect the value of the binding from the view closest to focus.

## Topics

### Creating the binding

`init(KeyPath<FocusedValues, Binding<Value>?>)`

A new property wrapper for the given key path.

### Getting the value

`var projectedValue: Binding<Value?>`

A binding to the optional value.

`var wrappedValue: Value?`

The unwrapped value for the focus key given the current scope and state of the
focused view hierarchy.

## Relationships

### Conforms To

  * `DynamicProperty`

## See Also

### Managing focus state

`func focused<Value>(FocusState<Value>.Binding, equals: Value) -> some View`

Modifies this view by binding its focus state to the given state value.

`func focused(FocusState<Bool>.Binding) -> some View`

Modifies this view by binding its focus state to the given Boolean state
value.

`var isFocused: Bool`

Returns whether the nearest focusable ancestor has focus.

`struct FocusState`

A property wrapper type that can read and write a value that SwiftUI updates
as the placement of focus within the scene changes.

`struct FocusedValue`

A property wrapper for observing values from the focused view or one of its
ancestors.

`protocol FocusedValueKey`

A protocol for identifier types used when publishing and observing focused
values.

Instance Method

# focusedValue(_:)

Sets the focused value for the given object type.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func focusedValue<T>(_ object: T?) -> some View where T : AnyObject, T : Observable
    

## Discussion

Important

This initializer only accepts objects conforming to the `Observable` protocol.
For reading environment objects that conform to `ObservableObject`, use
`focusedObject(_:)`, instead.

To read this value, use the `FocusedValue` property wrapper.

## See Also

### Exposing value types to focused views

`func focusedValue<Value>(WritableKeyPath<FocusedValues, Value?>, Value) ->
some View`

Modifies this view by injecting a value that you provide for use by other
views whose state depends on the focused view hierarchy.

`func focusedValue<Value>(WritableKeyPath<FocusedValues, Value?>, Value?) ->
some View`

Creates a new view that exposes the provided value to other views whose state
depends on the focused view hierarchy.

`func focusedSceneValue<T>(WritableKeyPath<FocusedValues, T?>, T?) -> some
View`

Creates a new view that exposes the provided value to other views whose state
depends on the active scene.

`func focusedSceneValue<T>(WritableKeyPath<FocusedValues, T?>, T) -> some
View`

Modifies this view by injecting a value that you provide for use by other
views whose state depends on the focused scene.

`struct FocusedValues`

A collection of state exported by the focused view and its ancestors.

Instance Method

# focusedValue(_:_:)

Modifies this view by injecting a value that you provide for use by other
views whose state depends on the focused view hierarchy.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    func focusedValue<Value>(
        _ keyPath: WritableKeyPath<FocusedValues, Value?>,
        _ value: Value
    ) -> some View
    

##  Parameters

`keyPath`

    

The key path to associate `value` with when adding it to the existing table of
exported focus values.

`value`

    

The focus value to export.

## Return Value

A modified representation of this view.

## See Also

### Exposing value types to focused views

`func focusedValue<T>(T?) -> some View`

Sets the focused value for the given object type.

`func focusedValue<Value>(WritableKeyPath<FocusedValues, Value?>, Value?) ->
some View`

Creates a new view that exposes the provided value to other views whose state
depends on the focused view hierarchy.

`func focusedSceneValue<T>(WritableKeyPath<FocusedValues, T?>, T?) -> some
View`

Creates a new view that exposes the provided value to other views whose state
depends on the active scene.

`func focusedSceneValue<T>(WritableKeyPath<FocusedValues, T?>, T) -> some
View`

Modifies this view by injecting a value that you provide for use by other
views whose state depends on the focused scene.

`struct FocusedValues`

A collection of state exported by the focused view and its ancestors.

Instance Method

# focusedValue(_:_:)

Creates a new view that exposes the provided value to other views whose state
depends on the focused view hierarchy.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func focusedValue<Value>(
        _ keyPath: WritableKeyPath<FocusedValues, Value?>,
        _ value: Value?
    ) -> some View
    

##  Parameters

`keyPath`

    

The key path to associate `value` with when adding it to the existing table of
exported focus values.

`value`

    

The focus value to export, or `nil` if no value is currently available.

## Return Value

A modified representation of this view.

## Discussion

Use this method instead of `View/focusedSceneValue(_:_:)` when your scene
includes multiple focusable views with their own associated values, and you
need an app- or scene-scoped element like a command or toolbar item that
operates on the value associated with whichever view currently has focus. Each
focusable view can supply its own value:

## See Also

### Exposing value types to focused views

`func focusedValue<T>(T?) -> some View`

Sets the focused value for the given object type.

`func focusedValue<Value>(WritableKeyPath<FocusedValues, Value?>, Value) ->
some View`

Modifies this view by injecting a value that you provide for use by other
views whose state depends on the focused view hierarchy.

`func focusedSceneValue<T>(WritableKeyPath<FocusedValues, T?>, T?) -> some
View`

Creates a new view that exposes the provided value to other views whose state
depends on the active scene.

`func focusedSceneValue<T>(WritableKeyPath<FocusedValues, T?>, T) -> some
View`

Modifies this view by injecting a value that you provide for use by other
views whose state depends on the focused scene.

`struct FocusedValues`

A collection of state exported by the focused view and its ancestors.

Instance Method

# focusedSceneValue(_:_:)

Creates a new view that exposes the provided value to other views whose state
depends on the active scene.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func focusedSceneValue<T>(
        _ keyPath: WritableKeyPath<FocusedValues, T?>,
        _ value: T?
    ) -> some View
    

##  Parameters

`keyPath`

    

The key path to associate `value` with when adding it to the existing table of
published focus values.

`value`

    

The focus value to publish, or `nil` if no value is currently available.

## Return Value

A modified representation of this view.

## Discussion

Use this method instead of `View/focusedValue(_:_:)` for values that must be
visible regardless of where focus is located in the active scene. For example,
if an app needs a command for moving focus to a particular text field in the
sidebar, it could use this modifier to publish a button action that’s visible
to command views as long as the scene is active, and regardless of where focus
happens to be in it.

    
    
    struct Sidebar: View {
        @FocusState var isFiltering: Bool
    
    
        var body: some View {
            VStack {
                TextField(...)
                    .focused(when: $isFiltering)
                    .focusedSceneValue(\.filterAction) {
                        isFiltering = true
                    }
            }
        }
    }
    
    
    struct NavigationCommands: Commands {
        @FocusedValue(\.filterAction) var filterAction
    
    
        var body: some Commands {
            CommandMenu("Navigate") {
                Button("Filter in Sidebar") {
                    filterAction?()
                }
            }
            .disabled(filterAction == nil)
        }
    }
    
    
    struct FilterActionKey: FocusedValuesKey {
        typealias Value = () -> Void
    }
    
    
    extension FocusedValues {
        var filterAction: (() -> Void)? {
            get { self[FilterActionKey.self] }
            set { self[FilterActionKey.self] = newValue }
        }
    }
    

## See Also

### Exposing value types to focused views

`func focusedValue<T>(T?) -> some View`

Sets the focused value for the given object type.

`func focusedValue<Value>(WritableKeyPath<FocusedValues, Value?>, Value) ->
some View`

Modifies this view by injecting a value that you provide for use by other
views whose state depends on the focused view hierarchy.

`func focusedValue<Value>(WritableKeyPath<FocusedValues, Value?>, Value?) ->
some View`

Creates a new view that exposes the provided value to other views whose state
depends on the focused view hierarchy.

`func focusedSceneValue<T>(WritableKeyPath<FocusedValues, T?>, T) -> some
View`

Modifies this view by injecting a value that you provide for use by other
views whose state depends on the focused scene.

`struct FocusedValues`

A collection of state exported by the focused view and its ancestors.

Instance Method

# focusedSceneValue(_:_:)

Modifies this view by injecting a value that you provide for use by other
views whose state depends on the focused scene.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func focusedSceneValue<T>(
        _ keyPath: WritableKeyPath<FocusedValues, T?>,
        _ value: T
    ) -> some View
    

##  Parameters

`keyPath`

    

The key path to associate `value` with when adding it to the existing table of
published focus values.

`value`

    

The focus value to publish.

## Return Value

A modified representation of this view.

## Discussion

Use this method instead of `View/focusedValue(_:_:)` for values that must be
visible regardless of where focus is located in the active scene. For example,
if an app needs a command for moving focus to a particular text field in the
sidebar, it could use this modifier to publish a button action that’s visible
to command views as long as the scene is active, and regardless of where focus
happens to be in it.

## See Also

### Exposing value types to focused views

`func focusedValue<T>(T?) -> some View`

Sets the focused value for the given object type.

`func focusedValue<Value>(WritableKeyPath<FocusedValues, Value?>, Value) ->
some View`

Modifies this view by injecting a value that you provide for use by other
views whose state depends on the focused view hierarchy.

`func focusedValue<Value>(WritableKeyPath<FocusedValues, Value?>, Value?) ->
some View`

Creates a new view that exposes the provided value to other views whose state
depends on the focused view hierarchy.

`func focusedSceneValue<T>(WritableKeyPath<FocusedValues, T?>, T?) -> some
View`

Creates a new view that exposes the provided value to other views whose state
depends on the active scene.

`struct FocusedValues`

A collection of state exported by the focused view and its ancestors.

Structure

# FocusedValues

A collection of state exported by the focused view and its ancestors.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    struct FocusedValues

## Topics

### Getting the value for a key

`subscript<Key>(Key.Type) -> Key.Value?`

Reads and writes values associated with a given focused value key.

## Relationships

### Conforms To

  * `Equatable`

## See Also

### Exposing value types to focused views

`func focusedValue<T>(T?) -> some View`

Sets the focused value for the given object type.

`func focusedValue<Value>(WritableKeyPath<FocusedValues, Value?>, Value) ->
some View`

Modifies this view by injecting a value that you provide for use by other
views whose state depends on the focused view hierarchy.

`func focusedValue<Value>(WritableKeyPath<FocusedValues, Value?>, Value?) ->
some View`

Creates a new view that exposes the provided value to other views whose state
depends on the focused view hierarchy.

`func focusedSceneValue<T>(WritableKeyPath<FocusedValues, T?>, T?) -> some
View`

Creates a new view that exposes the provided value to other views whose state
depends on the active scene.

`func focusedSceneValue<T>(WritableKeyPath<FocusedValues, T?>, T) -> some
View`

Modifies this view by injecting a value that you provide for use by other
views whose state depends on the focused scene.

Instance Method

# focusedObject(_:)

Creates a new view that exposes the provided object to other views whose state
depends on the focused view hierarchy.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func focusedObject<T>(_ object: T?) -> some View where T : ObservableObject
    

##  Parameters

`object`

    

The observable object to associate with focus, or `nil` if no object is
currently available.

## Return Value

A view that supplies an observable object when in focus.

## Discussion

Use this method instead of `View/focusedSceneObject(_:)` when your scene
includes multiple focusable views with their own associated data, and you need
an app- or scene-scoped element like a command or toolbar item that operates
on the data associated with whichever view currently has focus. Each focusable
view can supply its own object:

Interested views can then use the `FocusedObject` property wrapper to observe
and update the focused view’s object. In this example, an app command updates
the focused view’s data, and is automatically disabled when focus is in an
unrelated part of the scene:

## See Also

### Exposing reference types to focused views

`func focusedObject<T>(T) -> some View`

Creates a new view that exposes the provided object to other views whose whose
state depends on the focused view hierarchy.

`func focusedSceneObject<T>(T?) -> some View`

Creates a new view that exposes the provided object to other views whose whose
state depends on the active scene.

`func focusedSceneObject<T>(T) -> some View`

Creates a new view that exposes the provided object to other views whose whose
state depends on the active scene.

`struct FocusedObject`

A property wrapper type for an observable object supplied by the focused view
or one of its ancestors.

Instance Method

# focusedObject(_:)

Creates a new view that exposes the provided object to other views whose whose
state depends on the focused view hierarchy.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func focusedObject<T>(_ object: T) -> some View where T : ObservableObject
    

##  Parameters

`object`

    

The observable object to associate with focus.

## Return Value

A view that supplies an observable object when in focus.

## Discussion

Use this method instead of `View/focusedSceneObject(_:)` when your scene
includes multiple focusable views with their own associated data, and you need
an app- or scene-scoped element like a command or toolbar item that operates
on the data associated with whichever view currently has focus. Each focusable
view can supply its own object:

Interested views can then use the `FocusedObject` property wrapper to observe
and update the focused view’s object. In this example, an app command updates
the focused view’s data, and is automatically disabled when focus is in an
unrelated part of the scene:

## See Also

### Exposing reference types to focused views

`func focusedObject<T>(T?) -> some View`

Creates a new view that exposes the provided object to other views whose state
depends on the focused view hierarchy.

`func focusedSceneObject<T>(T?) -> some View`

Creates a new view that exposes the provided object to other views whose whose
state depends on the active scene.

`func focusedSceneObject<T>(T) -> some View`

Creates a new view that exposes the provided object to other views whose whose
state depends on the active scene.

`struct FocusedObject`

A property wrapper type for an observable object supplied by the focused view
or one of its ancestors.

Instance Method

# focusedSceneObject(_:)

Creates a new view that exposes the provided object to other views whose whose
state depends on the active scene.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func focusedSceneObject<T>(_ object: T?) -> some View where T : ObservableObject
    

##  Parameters

`object`

    

The observable object to associate with the scene, or `nil` if no object is
currently available.

## Return Value

A view that supplies an observable object while the scene is active.

## Discussion

Use this method instead of `View/focusedObject(_:)` for observable objects
that must be visible regardless of where focus is located in the active scene.
This is sometimes needed for things like main menu and discoverability HUD
commands that observe and update data from the active scene but aren’t
concerned with what the user is actually focused on. The scene’s root view can
supply the scene’s state object:

Interested views can then use the `FocusedObject` property wrapper to observe
and update the active scene’s state object. In this example, an app command
updates the active scene’s data, and is enabled as long as any scene is
active.

## See Also

### Exposing reference types to focused views

`func focusedObject<T>(T?) -> some View`

Creates a new view that exposes the provided object to other views whose state
depends on the focused view hierarchy.

`func focusedObject<T>(T) -> some View`

Creates a new view that exposes the provided object to other views whose whose
state depends on the focused view hierarchy.

`func focusedSceneObject<T>(T) -> some View`

Creates a new view that exposes the provided object to other views whose whose
state depends on the active scene.

`struct FocusedObject`

A property wrapper type for an observable object supplied by the focused view
or one of its ancestors.

Instance Method

# focusedSceneObject(_:)

Creates a new view that exposes the provided object to other views whose whose
state depends on the active scene.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func focusedSceneObject<T>(_ object: T) -> some View where T : ObservableObject
    

##  Parameters

`object`

    

The observable object to associate with the scene.

## Return Value

A view that supplies an observable object while the scene is active.

## Discussion

Use this method instead of `View/focusedObject(_:)` for observable objects
that must be visible regardless of where focus is located in the active scene.
This is sometimes needed for things like main menu and discoverability HUD
commands that observe and update data from the active scene but aren’t
concerned with what the user is actually focused on. The scene’s root view can
supply the scene’s state object:

Interested views can then use the `FocusedObject` property wrapper to observe
and update the active scene’s state object. In this example, an app command
updates the active scene’s data, and is enabled as long as any scene is
active.

## See Also

### Exposing reference types to focused views

`func focusedObject<T>(T?) -> some View`

Creates a new view that exposes the provided object to other views whose state
depends on the focused view hierarchy.

`func focusedObject<T>(T) -> some View`

Creates a new view that exposes the provided object to other views whose whose
state depends on the focused view hierarchy.

`func focusedSceneObject<T>(T?) -> some View`

Creates a new view that exposes the provided object to other views whose whose
state depends on the active scene.

`struct FocusedObject`

A property wrapper type for an observable object supplied by the focused view
or one of its ancestors.

Structure

# FocusedObject

A property wrapper type for an observable object supplied by the focused view
or one of its ancestors.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    @frozen @propertyWrapper
    struct FocusedObject<ObjectType> where ObjectType : ObservableObject

## Overview

Focused objects invalidate the current view whenever the observable object
changes. If multiple views publish a focused object using the same key, the
wrapped property will reflect the object that’s closest to the focused view.

## Topics

### Creating the focused object

`init()`

Creates a focused object.

### Getting the value

`var projectedValue: FocusedObject<ObjectType>.Wrapper?`

A projection of the focused object that creates bindings to its properties
using dynamic member lookup.

`var wrappedValue: ObjectType?`

The underlying value referenced by the focused object.

`struct Wrapper`

A wrapper around the underlying focused object that can create bindings to its
properties using dynamic member lookup.

## Relationships

### Conforms To

  * `DynamicProperty`

## See Also

### Exposing reference types to focused views

`func focusedObject<T>(T?) -> some View`

Creates a new view that exposes the provided object to other views whose state
depends on the focused view hierarchy.

`func focusedObject<T>(T) -> some View`

Creates a new view that exposes the provided object to other views whose whose
state depends on the focused view hierarchy.

`func focusedSceneObject<T>(T?) -> some View`

Creates a new view that exposes the provided object to other views whose whose
state depends on the active scene.

`func focusedSceneObject<T>(T) -> some View`

Creates a new view that exposes the provided object to other views whose whose
state depends on the active scene.

Instance Method

# focusScope(_:)

Creates a focus scope that SwiftUI uses to limit default focus preferences.

macOS 12.0+  tvOS 14.0+  watchOS 7.0+

    
    
    func focusScope(_ namespace: Namespace.ID) -> some View
    

##  Parameters

`namespace`

    

A namespace identifier that SwiftUI can use to scope default focus
preferences.

## Return Value

A view that sets the namespace of descendants for default focus.

## Discussion

The returned view gets associated with the provided namespace. Pass this
namespace to `prefersDefaultFocus(_:in:)` and the `resetFocus` function.

## See Also

### Setting focus scope

`func focusSection() -> some View`

Indicates that the view’s frame and cohort of focusable descendants should be
used to guide focus movement.

Instance Method

# focusSection()

Indicates that the view’s frame and cohort of focusable descendants should be
used to guide focus movement.

macOS 13.0+  tvOS 15.0+

    
    
    func focusSection() -> some View
    

## Return Value

A view that can guide focus to its focusable descendents.

## Discussion

Use focus sections to customize SwiftUI’s behavior when the user moves focus
between views.

The following tvOS example places three buttons (“1”, “2”, and “3”) at the
upper left of the screen and three buttons (“A”, “B”, and “C”) at the bottom
right. By default, swiping right on the Siri Remote on any of the buttons in
the “1” - “3” group would do nothing, since the focus system finds no
focusable views directly to their right. But by declaring the `VStack` that
encloses buttons “A” - “C” as a focus section, the `VStack` can receive focus,
and deliver that focus to its first focusable child (button “A”). The example
puts a border on the `VStack` to illustrate this spatial arrangement.

Note that because the `VStack` containing buttons “1” - “3” does not declare
itself as a focus section, it is impossible to direct focus back to the left
from buttons “A” - “C”. None of those buttons has a focusable view — in this
case either a button or a `VStack` with the `focusSection()` modifier —
directly to its left.

Applying this modifier to a view affects focus behavior based on the style of
movement:

  * **Directional movement** : Navigating with Siri Remote gestures, arrow keys on a keyboard, or any other type of input that works in terms of cardinal directions (up, down, left, right) produces directional movement. When modified with `focusSection()`, the view’s frame becomes capable of accepting focus in order to direct it at its nearest focusable descendant in the direction of travel. In the earlier example, declaring the right-side `VStack` as a focus section allowed it to receive right-directed focus from the buttons on the left.

  * **Sequential movement** : Navigating with a Digital Crown, the Tab key on a keyboard, or any other type of input that works in terms of the next or previous item in a sequence, produces sequential movement. When you use the `focusSection()` modifier, SwiftUI deviates from its default layout-based sequence to visit each of the modified view’s focusable descendants before resuming the default sequence. Within the set of focusable descendants, SwiftUI continues to visit views in layout order (leading-to-trailing, top-to-bottom).

`focusSection()` does not affect the focusability of the modified view. If the
modified view has no focusable descendants, then the modifier does nothing.

## See Also

### Setting focus scope

`func focusScope(Namespace.ID) -> some View`

Creates a focus scope that SwiftUI uses to limit default focus preferences.

Instance Method

# prefersDefaultFocus(_:in:)

Indicates that the view should receive focus by default for a given namespace.

macOS 12.0+  tvOS 14.0+  watchOS 7.0+

    
    
    func prefersDefaultFocus(
        _ prefersDefaultFocus: Bool = true,
        in namespace: Namespace.ID
    ) -> some View
    

##  Parameters

`prefersDefaultFocus`

    

A Boolean value that indicates whether this view prefers to receive focus by
default. The default value, `true`, causes the view to receive focus by
default.

`namespace`

    

The namespace associated with the focus scope within which this view prefers
default focus.

## Return Value

A modified view that sets whether it prefers to be focused by default.

## Discussion

This modifier sets the initial focus preference when no other view has focus.
Use the environment value `resetFocus` to force a reevaluation of default
focus at any time.

The following tvOS example shows three buttons, labeled “1”, “2”, and “3”, in
a `VStack`. By default, the “1” button would receive focus, because it is the
first child in the stack. However, the `prefersDefaultFocus(_:in:)` modifier
allows button “3” to receive default focus instead. Once the buttons are
visible, the user can move down to and focus the “Reset to default focus”
button. When the user activates this button, it uses the `ResetFocusAction` to
reevaluate default focus in the `mainNamespace`, which returns the focus to
button “3”.

The default focus preference is limited to the focusable ancestor that matches
the provided namespace. If multiple views express this preference, then
SwiftUI applies the current platform rules to determine which view receives
focus.

## See Also

### Controlling default focus

`func defaultFocus<V>(FocusState<V>.Binding, V, priority:
DefaultFocusEvaluationPriority) -> some View`

Defines a region of the window in which default focus is evaluated by
assigning a value to a given focus state binding.

`struct DefaultFocusEvaluationPriority`

Prioritizations for default focus preferences when evaluating where to move
focus in different circumstances.

Instance Method

# defaultFocus(_:_:priority:)

Defines a region of the window in which default focus is evaluated by
assigning a value to a given focus state binding.

iOS 17.0+  iPadOS 17.0+  macOS 13.0+  Mac Catalyst 17.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func defaultFocus<V>(
        _ binding: FocusState<V>.Binding,
        _ value: V,
        priority: DefaultFocusEvaluationPriority = .automatic
    ) -> some View where V : Hashable
    

##  Parameters

`binding`

    

A focus state binding to update when evaluating default focus in the modified
view hierarchy.

`value`

    

The value to set the binding to during evaluation.

`priority`

    

An indication of how to prioritize the preferred default focus target when
focus moves into the modified view hierarchy. The default value is
`automatic`, which means the preference will be given priority when focus is
being initialized or relocated programmatically, but not when responding to
user-directed navigation commands.

## Return Value

The modified view.

## Discussion

By default, SwiftUI evaluates default focus when the window first appears, and
when a focus state binding update moves focus automatically, but not when
responding to user-driven navigation commands.

Clients can override the default behavior by specifying an evaluation priority
of `userInitiated`, which causes SwiftUI to use the client’s preferred default
focus in response to user-driven focus navigation as well as automatic
changes.

In the following example, focus automatically goes to the second of the two
text fields when the view is first presented in the window.

## See Also

### Controlling default focus

`func prefersDefaultFocus(Bool, in: Namespace.ID) -> some View`

Indicates that the view should receive focus by default for a given namespace.

`struct DefaultFocusEvaluationPriority`

Prioritizations for default focus preferences when evaluating where to move
focus in different circumstances.

Structure

# DefaultFocusEvaluationPriority

Prioritizations for default focus preferences when evaluating where to move
focus in different circumstances.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    struct DefaultFocusEvaluationPriority

## Topics

### Getting the priorities

`static let automatic: DefaultFocusEvaluationPriority`

Use the default focus preference when focus moves into the affected branch
automatically, but ignore it when the movement is driven by a user-initiated
navigation command.

`static let userInitiated: DefaultFocusEvaluationPriority`

Always use the default focus preference when focus moves into the affected
branch.

## Relationships

### Conforms To

  * `Sendable`

## See Also

### Controlling default focus

`func prefersDefaultFocus(Bool, in: Namespace.ID) -> some View`

Indicates that the view should receive focus by default for a given namespace.

`func defaultFocus<V>(FocusState<V>.Binding, V, priority:
DefaultFocusEvaluationPriority) -> some View`

Defines a region of the window in which default focus is evaluated by
assigning a value to a given focus state binding.

Instance Property

# resetFocus

An action that requests the focus system to reevaluate default focus.

macOS 12.0+  tvOS 14.0+  watchOS 7.0+

    
    
    var resetFocus: ResetFocusAction { get }

## Discussion

Get this environment value and call and call it as a function to force a
default focus reevaluation at runtime.

## See Also

### Resetting focus

`struct ResetFocusAction`

An environment value that provides the ability to reevaluate default focus.

Structure

# ResetFocusAction

An environment value that provides the ability to reevaluate default focus.

macOS 12.0+  tvOS 14.0+  watchOS 7.0+

    
    
    struct ResetFocusAction

## Overview

Get the `resetFocus` environment value and call it as a function to force a
default focus reevaluation at runtime.

## Topics

### Calling the action

`func callAsFunction(in: Namespace.ID)`

Asks the focus sytem to reevaluate the default focus item.

## See Also

### Resetting focus

`var resetFocus: ResetFocusAction`

An action that requests the focus system to reevaluate default focus.

Instance Method

# focusEffectDisabled(_:)

Adds a condition that controls whether this view can display focus effects,
such as a default focus ring or hover effect.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func focusEffectDisabled(_ disabled: Bool = true) -> some View
    

##  Parameters

`disabled`

    

A Boolean value that determines whether this view can display focus effects.

## Return Value

A view that controls whether focus effects can be displayed in this view.

## Discussion

The higher views in a view hierarchy can override the value you set on this
view. In the following example, the button does not display a focus effect
because the outer `focusEffectDisabled(_:)` modifier overrides the inner one:

## See Also

### Configuring effects

`var isFocusEffectEnabled: Bool`

A Boolean value that indicates whether the view associated with this
environment allows focus effects to be displayed.

Instance Property

# isFocusEffectEnabled

A Boolean value that indicates whether the view associated with this
environment allows focus effects to be displayed.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    var isFocusEffectEnabled: Bool { get set }

## Discussion

The default value is `true`.

## See Also

### Configuring effects

`func focusEffectDisabled(Bool) -> some View`

Adds a condition that controls whether this view can display focus effects,
such as a default focus ring or hover effect.



# FormStyle

Type Property

# automatic

The default form style.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    static var automatic: AutomaticFormStyle { get }

Available when `Self` is `AutomaticFormStyle`.

## See Also

### Getting built-in form styles

`static var columns: ColumnsFormStyle`

A non-scrolling form style with a trailing aligned column of labels next to a
leading aligned column of values.

Available when `Self` is `ColumnsFormStyle`.

`static var grouped: GroupedFormStyle`

A form style with grouped rows.

Available when `Self` is `GroupedFormStyle`.

Type Property

# columns

A non-scrolling form style with a trailing aligned column of labels next to a
leading aligned column of values.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    static var columns: ColumnsFormStyle { get }

Available when `Self` is `ColumnsFormStyle`.

## See Also

### Getting built-in form styles

`static var automatic: AutomaticFormStyle`

The default form style.

Available when `Self` is `AutomaticFormStyle`.

`static var grouped: GroupedFormStyle`

A form style with grouped rows.

Available when `Self` is `GroupedFormStyle`.

Type Property

# grouped

A form style with grouped rows.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    static var grouped: GroupedFormStyle { get }

Available when `Self` is `GroupedFormStyle`.

## Discussion

Rows in a grouped rows form have leading aligned labels and trailing aligned
controls within visually grouped sections.

## See Also

### Getting built-in form styles

`static var automatic: AutomaticFormStyle`

The default form style.

Available when `Self` is `AutomaticFormStyle`.

`static var columns: ColumnsFormStyle`

A non-scrolling form style with a trailing aligned column of labels next to a
leading aligned column of values.

Available when `Self` is `ColumnsFormStyle`.

Instance Method

# makeBody(configuration:)

Creates a view that represents the body of a form.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    @ViewBuilder
    func makeBody(configuration: Self.Configuration) -> Self.Body

**Required**

##  Parameters

`configuration`

    

The properties of the form.

## Return Value

A view that has behavior and appearance that enables it to function as a
`Form`.

## See Also

### Creating custom form styles

`typealias Configuration`

The properties of a form instance.

`associatedtype Body : View`

A view that represents the appearance and interaction of a form.

**Required**

Type Alias

# FormStyle.Configuration

The properties of a form instance.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    typealias Configuration = FormStyleConfiguration

## Discussion

You receive a `configuration` parameter of this type — which is an alias for
the `FormStyleConfiguration` type — when you implement the required
`makeBody(configuration:)` method in a custom form style implementation.

## See Also

### Creating custom form styles

`func makeBody(configuration: Self.Configuration) -> Self.Body`

Creates a view that represents the body of a form.

**Required**

` associatedtype Body : View`

A view that represents the appearance and interaction of a form.

**Required**

Associated Type

# Body

A view that represents the appearance and interaction of a form.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    associatedtype Body : View

**Required**

## See Also

### Creating custom form styles

`func makeBody(configuration: Self.Configuration) -> Self.Body`

Creates a view that represents the body of a form.

**Required**

` typealias Configuration`

The properties of a form instance.

Structure

# AutomaticFormStyle

The default form style.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    struct AutomaticFormStyle

## Overview

Use the `automatic` static variable to create this style:

## Topics

### Creating the form style

`init()`

Creates a default form style.

## Relationships

### Conforms To

  * `FormStyle`

## See Also

### Supporting types

`struct ColumnsFormStyle`

A non-scrolling form style with a trailing aligned column of labels next to a
leading aligned column of values.

`struct GroupedFormStyle`

A form style with grouped rows.

Structure

# ColumnsFormStyle

A non-scrolling form style with a trailing aligned column of labels next to a
leading aligned column of values.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    struct ColumnsFormStyle

## Overview

Use the `columns` static variable to create this style:

## Topics

### Creating the form style

`init()`

A non-scrolling form style with a trailing aligned column of labels next to a
leading aligned column of values.

## Relationships

### Conforms To

  * `FormStyle`

## See Also

### Supporting types

`struct AutomaticFormStyle`

The default form style.

`struct GroupedFormStyle`

A form style with grouped rows.

Structure

# GroupedFormStyle

A form style with grouped rows.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    struct GroupedFormStyle

## Overview

Rows in this form style have leading aligned labels and trailing aligned
controls within visually grouped sections.

Use the `grouped` static variable to create this style:

## Topics

### Creating the form style

`init()`

Creates a form style with scrolling, grouped rows.

## Relationships

### Conforms To

  * `FormStyle`

## See Also

### Supporting types

`struct AutomaticFormStyle`

The default form style.

`struct ColumnsFormStyle`

A non-scrolling form style with a trailing aligned column of labels next to a
leading aligned column of values.



# FieldDatePickerStyle

Initializer

# init()

Creates an instance of the field date picker style.

macOS 10.15+

    
    
    init()



# FullImmersionStyle

Initializer

# init()

visionOS 1.0+

    
    
    init()



# Font.Leading

Case

# Font.Leading.standard

The font’s default line spacing.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    case standard

## Discussion

If you modify a font to use a nonstandard line spacing like
`Font.Leading.tight` or `Font.Leading.loose`, you can use this value to return
to the font’s default line spacing.

## See Also

### Getting leading line spacing options

`case loose`

Increased line spacing.

`case tight`

Reduced line spacing.

Case

# Font.Leading.loose

Increased line spacing.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    case loose

## Discussion

This value typically increases line spacing by 1 point for watchOS and 2
points on other platforms.

## See Also

### Getting leading line spacing options

`case standard`

The font’s default line spacing.

`case tight`

Reduced line spacing.

Case

# Font.Leading.tight

Reduced line spacing.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    case tight

## Discussion

This value typically reduces line spacing by 1 point for watchOS and 2 points
on other platforms.

## See Also

### Getting leading line spacing options

`case standard`

The font’s default line spacing.

`case loose`

Increased line spacing.



# FileDialogBrowserOptions

Type Property

# displayFileExtensions

On iOS, configures the `fileExporter`, `fileImporter`, or `fileMover` to show
or hide file extensions. Default behavior is to hide them. On macOS, this
option has no effect.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    static let displayFileExtensions: FileDialogBrowserOptions

## See Also

### Getting browser options

`static let enumeratePackages: FileDialogBrowserOptions`

Allows enumerating packages contents in contrast to the default behavior when
packages are represented flatly, similar to files.

`static let includeHiddenFiles: FileDialogBrowserOptions`

Displays the files that are hidden by default.

Type Property

# enumeratePackages

Allows enumerating packages contents in contrast to the default behavior when
packages are represented flatly, similar to files.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    static let enumeratePackages: FileDialogBrowserOptions

## See Also

### Getting browser options

`static let displayFileExtensions: FileDialogBrowserOptions`

On iOS, configures the `fileExporter`, `fileImporter`, or `fileMover` to show
or hide file extensions. Default behavior is to hide them. On macOS, this
option has no effect.

`static let includeHiddenFiles: FileDialogBrowserOptions`

Displays the files that are hidden by default.

Type Property

# includeHiddenFiles

Displays the files that are hidden by default.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    static let includeHiddenFiles: FileDialogBrowserOptions

## See Also

### Getting browser options

`static let displayFileExtensions: FileDialogBrowserOptions`

On iOS, configures the `fileExporter`, `fileImporter`, or `fileMover` to show
or hide file extensions. Default behavior is to hide them. On macOS, this
option has no effect.

`static let enumeratePackages: FileDialogBrowserOptions`

Allows enumerating packages contents in contrast to the default behavior when
packages are represented flatly, similar to files.



# ForegroundStyle

Initializer

# init()

Creates a foreground style instance.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init()



# FetchRequest.Configuration

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



# Font.TextStyle

Case

# Font.TextStyle.extraLargeTitle2

The font used for second level extra large titles.

visionOS 1.0+

    
    
    case extraLargeTitle2

## See Also

### Getting font text styles

`case extraLargeTitle`

The font used for extra large titles.

`case largeTitle`

The font style for large titles.

`case title`

The font used for first level hierarchical headings.

`case title2`

The font used for second level hierarchical headings.

`case title3`

The font used for third level hierarchical headings.

`case headline`

The font used for headings.

`case subheadline`

The font used for subheadings.

`case body`

The font used for body text.

`case callout`

The font used for callouts.

`case caption`

The font used for standard captions.

`case caption2`

The font used for alternate captions.

`case footnote`

The font used in footnotes.

Case

# Font.TextStyle.extraLargeTitle

The font used for extra large titles.

visionOS 1.0+

    
    
    case extraLargeTitle

## See Also

### Getting font text styles

`case extraLargeTitle2`

The font used for second level extra large titles.

`case largeTitle`

The font style for large titles.

`case title`

The font used for first level hierarchical headings.

`case title2`

The font used for second level hierarchical headings.

`case title3`

The font used for third level hierarchical headings.

`case headline`

The font used for headings.

`case subheadline`

The font used for subheadings.

`case body`

The font used for body text.

`case callout`

The font used for callouts.

`case caption`

The font used for standard captions.

`case caption2`

The font used for alternate captions.

`case footnote`

The font used in footnotes.

Case

# Font.TextStyle.largeTitle

The font style for large titles.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    case largeTitle

## See Also

### Getting font text styles

`case extraLargeTitle2`

The font used for second level extra large titles.

`case extraLargeTitle`

The font used for extra large titles.

`case title`

The font used for first level hierarchical headings.

`case title2`

The font used for second level hierarchical headings.

`case title3`

The font used for third level hierarchical headings.

`case headline`

The font used for headings.

`case subheadline`

The font used for subheadings.

`case body`

The font used for body text.

`case callout`

The font used for callouts.

`case caption`

The font used for standard captions.

`case caption2`

The font used for alternate captions.

`case footnote`

The font used in footnotes.

Case

# Font.TextStyle.title

The font used for first level hierarchical headings.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    case title

## See Also

### Getting font text styles

`case extraLargeTitle2`

The font used for second level extra large titles.

`case extraLargeTitle`

The font used for extra large titles.

`case largeTitle`

The font style for large titles.

`case title2`

The font used for second level hierarchical headings.

`case title3`

The font used for third level hierarchical headings.

`case headline`

The font used for headings.

`case subheadline`

The font used for subheadings.

`case body`

The font used for body text.

`case callout`

The font used for callouts.

`case caption`

The font used for standard captions.

`case caption2`

The font used for alternate captions.

`case footnote`

The font used in footnotes.

Case

# Font.TextStyle.title2

The font used for second level hierarchical headings.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    case title2

## See Also

### Getting font text styles

`case extraLargeTitle2`

The font used for second level extra large titles.

`case extraLargeTitle`

The font used for extra large titles.

`case largeTitle`

The font style for large titles.

`case title`

The font used for first level hierarchical headings.

`case title3`

The font used for third level hierarchical headings.

`case headline`

The font used for headings.

`case subheadline`

The font used for subheadings.

`case body`

The font used for body text.

`case callout`

The font used for callouts.

`case caption`

The font used for standard captions.

`case caption2`

The font used for alternate captions.

`case footnote`

The font used in footnotes.

Case

# Font.TextStyle.title3

The font used for third level hierarchical headings.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    case title3

## See Also

### Getting font text styles

`case extraLargeTitle2`

The font used for second level extra large titles.

`case extraLargeTitle`

The font used for extra large titles.

`case largeTitle`

The font style for large titles.

`case title`

The font used for first level hierarchical headings.

`case title2`

The font used for second level hierarchical headings.

`case headline`

The font used for headings.

`case subheadline`

The font used for subheadings.

`case body`

The font used for body text.

`case callout`

The font used for callouts.

`case caption`

The font used for standard captions.

`case caption2`

The font used for alternate captions.

`case footnote`

The font used in footnotes.

Case

# Font.TextStyle.headline

The font used for headings.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    case headline

## See Also

### Getting font text styles

`case extraLargeTitle2`

The font used for second level extra large titles.

`case extraLargeTitle`

The font used for extra large titles.

`case largeTitle`

The font style for large titles.

`case title`

The font used for first level hierarchical headings.

`case title2`

The font used for second level hierarchical headings.

`case title3`

The font used for third level hierarchical headings.

`case subheadline`

The font used for subheadings.

`case body`

The font used for body text.

`case callout`

The font used for callouts.

`case caption`

The font used for standard captions.

`case caption2`

The font used for alternate captions.

`case footnote`

The font used in footnotes.

Case

# Font.TextStyle.subheadline

The font used for subheadings.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    case subheadline

## See Also

### Getting font text styles

`case extraLargeTitle2`

The font used for second level extra large titles.

`case extraLargeTitle`

The font used for extra large titles.

`case largeTitle`

The font style for large titles.

`case title`

The font used for first level hierarchical headings.

`case title2`

The font used for second level hierarchical headings.

`case title3`

The font used for third level hierarchical headings.

`case headline`

The font used for headings.

`case body`

The font used for body text.

`case callout`

The font used for callouts.

`case caption`

The font used for standard captions.

`case caption2`

The font used for alternate captions.

`case footnote`

The font used in footnotes.

Case

# Font.TextStyle.body

The font used for body text.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    case body

## See Also

### Getting font text styles

`case extraLargeTitle2`

The font used for second level extra large titles.

`case extraLargeTitle`

The font used for extra large titles.

`case largeTitle`

The font style for large titles.

`case title`

The font used for first level hierarchical headings.

`case title2`

The font used for second level hierarchical headings.

`case title3`

The font used for third level hierarchical headings.

`case headline`

The font used for headings.

`case subheadline`

The font used for subheadings.

`case callout`

The font used for callouts.

`case caption`

The font used for standard captions.

`case caption2`

The font used for alternate captions.

`case footnote`

The font used in footnotes.

Case

# Font.TextStyle.callout

The font used for callouts.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    case callout

## See Also

### Getting font text styles

`case extraLargeTitle2`

The font used for second level extra large titles.

`case extraLargeTitle`

The font used for extra large titles.

`case largeTitle`

The font style for large titles.

`case title`

The font used for first level hierarchical headings.

`case title2`

The font used for second level hierarchical headings.

`case title3`

The font used for third level hierarchical headings.

`case headline`

The font used for headings.

`case subheadline`

The font used for subheadings.

`case body`

The font used for body text.

`case caption`

The font used for standard captions.

`case caption2`

The font used for alternate captions.

`case footnote`

The font used in footnotes.

Case

# Font.TextStyle.caption

The font used for standard captions.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    case caption

## See Also

### Getting font text styles

`case extraLargeTitle2`

The font used for second level extra large titles.

`case extraLargeTitle`

The font used for extra large titles.

`case largeTitle`

The font style for large titles.

`case title`

The font used for first level hierarchical headings.

`case title2`

The font used for second level hierarchical headings.

`case title3`

The font used for third level hierarchical headings.

`case headline`

The font used for headings.

`case subheadline`

The font used for subheadings.

`case body`

The font used for body text.

`case callout`

The font used for callouts.

`case caption2`

The font used for alternate captions.

`case footnote`

The font used in footnotes.

Case

# Font.TextStyle.caption2

The font used for alternate captions.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    case caption2

## See Also

### Getting font text styles

`case extraLargeTitle2`

The font used for second level extra large titles.

`case extraLargeTitle`

The font used for extra large titles.

`case largeTitle`

The font style for large titles.

`case title`

The font used for first level hierarchical headings.

`case title2`

The font used for second level hierarchical headings.

`case title3`

The font used for third level hierarchical headings.

`case headline`

The font used for headings.

`case subheadline`

The font used for subheadings.

`case body`

The font used for body text.

`case callout`

The font used for callouts.

`case caption`

The font used for standard captions.

`case footnote`

The font used in footnotes.

Case

# Font.TextStyle.footnote

The font used in footnotes.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    case footnote

## See Also

### Getting font text styles

`case extraLargeTitle2`

The font used for second level extra large titles.

`case extraLargeTitle`

The font used for extra large titles.

`case largeTitle`

The font style for large titles.

`case title`

The font used for first level hierarchical headings.

`case title2`

The font used for second level hierarchical headings.

`case title3`

The font used for third level hierarchical headings.

`case headline`

The font used for headings.

`case subheadline`

The font used for subheadings.

`case body`

The font used for body text.

`case callout`

The font used for callouts.

`case caption`

The font used for standard captions.

`case caption2`

The font used for alternate captions.



# FocusedObject

Initializer

# init()

Creates a focused object.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    init()

Instance Property

# projectedValue

A projection of the focused object that creates bindings to its properties
using dynamic member lookup.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    @MainActor
    var projectedValue: FocusedObject<ObjectType>.Wrapper? { get }

## Discussion

Use the projected value to pass a focused object down a view hierarchy.

## See Also

### Getting the value

`var wrappedValue: ObjectType?`

The underlying value referenced by the focused object.

`struct Wrapper`

A wrapper around the underlying focused object that can create bindings to its
properties using dynamic member lookup.

Instance Property

# wrappedValue

The underlying value referenced by the focused object.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    @MainActor
    var wrappedValue: ObjectType? { get }

## Discussion

This property provides primary access to the value’s data. However, you don’t
access `wrappedValue` directly. Instead, you use the property variable created
with the `FocusedObject` attribute.

When a mutable value changes, the new value is immediately available. However,
a view displaying the value is updated asynchronously and may not show the new
value immediately.

## See Also

### Getting the value

`var projectedValue: FocusedObject<ObjectType>.Wrapper?`

A projection of the focused object that creates bindings to its properties
using dynamic member lookup.

`struct Wrapper`

A wrapper around the underlying focused object that can create bindings to its
properties using dynamic member lookup.

Structure

# FocusedObject.Wrapper

A wrapper around the underlying focused object that can create bindings to its
properties using dynamic member lookup.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    @dynamicMemberLookup @frozen
    struct Wrapper

## Topics

### Accessing members

`subscript<T>(dynamicMember _: ReferenceWritableKeyPath<ObjectType, T>) ->
Binding<T>`

Returns a binding to the value of a given key path.

## See Also

### Getting the value

`var projectedValue: FocusedObject<ObjectType>.Wrapper?`

A projection of the focused object that creates bindings to its properties
using dynamic member lookup.

`var wrappedValue: ObjectType?`

The underlying value referenced by the focused object.



# FocusedValues

Instance Subscript

# subscript(_:)

Reads and writes values associated with a given focused value key.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    subscript<Key>(key: Key.Type) -> Key.Value? where Key : FocusedValueKey { get set }



# FocusState

Initializer

# init()

Creates a focus state that binds to an optional type.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    init<T>() where Value == T?, T : Hashable

## See Also

### Creating a focus state

`init()`

Creates a focus state that binds to a Boolean.

Initializer

# init()

Creates a focus state that binds to a Boolean.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    init() where Value == Bool

## See Also

### Creating a focus state

`init<T>()`

Creates a focus state that binds to an optional type.

Instance Property

# projectedValue

A projection of the focus state value that returns a binding.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    var projectedValue: FocusState<Value>.Binding { get }

## Discussion

When focus is outside any view that is bound to this state, the wrapped value
is `nil` for optional-typed state or `false` for Boolean state.

In the following example of a simple navigation sidebar, when the user presses
the Filter Sidebar Contents button, focus moves to the sidebar’s filter text
field. Conversely, if the user moves focus to the sidebar’s filter manually,
then the value of `isFiltering` automatically becomes `true`, and the sidebar
view updates.

## See Also

### Inspecting the focus state

`struct Binding`

A property wrapper type that can read and write a value that indicates the
current focus location.

`var wrappedValue: Value`

The current state value, taking into account whatever bindings might be in
effect due to the current location of focus.

Structure

# FocusState.Binding

A property wrapper type that can read and write a value that indicates the
current focus location.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    @frozen @propertyWrapper
    struct Binding

## Topics

### Inspecting the binding

`var projectedValue: FocusState<Value>.Binding`

A projection of the binding value that returns a binding.

`var wrappedValue: Value`

The underlying value referenced by the bound property.

## See Also

### Inspecting the focus state

`var projectedValue: FocusState<Value>.Binding`

A projection of the focus state value that returns a binding.

`var wrappedValue: Value`

The current state value, taking into account whatever bindings might be in
effect due to the current location of focus.

Instance Property

# wrappedValue

The current state value, taking into account whatever bindings might be in
effect due to the current location of focus.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    var wrappedValue: Value { get nonmutating set }

## Discussion

When focus is not in any view that is bound to this state, the wrapped value
will be `nil` (for optional-typed state) or `false` (for `Bool`\- typed
state).

## See Also

### Inspecting the focus state

`var projectedValue: FocusState<Value>.Binding`

A projection of the focus state value that returns a binding.

`struct Binding`

A property wrapper type that can read and write a value that indicates the
current focus location.



# Font

Type Property

# extraLargeTitle2

Create a font with the second level extra large title text style.

visionOS 1.0+

    
    
    static let extraLargeTitle2: Font

## See Also

### Getting standard fonts

`static let extraLargeTitle: Font`

Create a font with the extra large title text style.

`static let largeTitle: Font`

A font with the large title text style.

`static let title: Font`

A font with the title text style.

`static let title2: Font`

Create a font for second level hierarchical headings.

`static let title3: Font`

Create a font for third level hierarchical headings.

`static let headline: Font`

A font with the headline text style.

`static let subheadline: Font`

A font with the subheadline text style.

`static let body: Font`

A font with the body text style.

`static let callout: Font`

A font with the callout text style.

`static let caption: Font`

A font with the caption text style.

`static let caption2: Font`

Create a font with the alternate caption text style.

`static let footnote: Font`

A font with the footnote text style.

Type Property

# extraLargeTitle

Create a font with the extra large title text style.

visionOS 1.0+

    
    
    static let extraLargeTitle: Font

## See Also

### Getting standard fonts

`static let extraLargeTitle2: Font`

Create a font with the second level extra large title text style.

`static let largeTitle: Font`

A font with the large title text style.

`static let title: Font`

A font with the title text style.

`static let title2: Font`

Create a font for second level hierarchical headings.

`static let title3: Font`

Create a font for third level hierarchical headings.

`static let headline: Font`

A font with the headline text style.

`static let subheadline: Font`

A font with the subheadline text style.

`static let body: Font`

A font with the body text style.

`static let callout: Font`

A font with the callout text style.

`static let caption: Font`

A font with the caption text style.

`static let caption2: Font`

Create a font with the alternate caption text style.

`static let footnote: Font`

A font with the footnote text style.

Type Property

# largeTitle

A font with the large title text style.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static let largeTitle: Font

## See Also

### Getting standard fonts

`static let extraLargeTitle2: Font`

Create a font with the second level extra large title text style.

`static let extraLargeTitle: Font`

Create a font with the extra large title text style.

`static let title: Font`

A font with the title text style.

`static let title2: Font`

Create a font for second level hierarchical headings.

`static let title3: Font`

Create a font for third level hierarchical headings.

`static let headline: Font`

A font with the headline text style.

`static let subheadline: Font`

A font with the subheadline text style.

`static let body: Font`

A font with the body text style.

`static let callout: Font`

A font with the callout text style.

`static let caption: Font`

A font with the caption text style.

`static let caption2: Font`

Create a font with the alternate caption text style.

`static let footnote: Font`

A font with the footnote text style.

Type Property

# title

A font with the title text style.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static let title: Font

## See Also

### Getting standard fonts

`static let extraLargeTitle2: Font`

Create a font with the second level extra large title text style.

`static let extraLargeTitle: Font`

Create a font with the extra large title text style.

`static let largeTitle: Font`

A font with the large title text style.

`static let title2: Font`

Create a font for second level hierarchical headings.

`static let title3: Font`

Create a font for third level hierarchical headings.

`static let headline: Font`

A font with the headline text style.

`static let subheadline: Font`

A font with the subheadline text style.

`static let body: Font`

A font with the body text style.

`static let callout: Font`

A font with the callout text style.

`static let caption: Font`

A font with the caption text style.

`static let caption2: Font`

Create a font with the alternate caption text style.

`static let footnote: Font`

A font with the footnote text style.

Type Property

# title2

Create a font for second level hierarchical headings.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    static let title2: Font

## See Also

### Getting standard fonts

`static let extraLargeTitle2: Font`

Create a font with the second level extra large title text style.

`static let extraLargeTitle: Font`

Create a font with the extra large title text style.

`static let largeTitle: Font`

A font with the large title text style.

`static let title: Font`

A font with the title text style.

`static let title3: Font`

Create a font for third level hierarchical headings.

`static let headline: Font`

A font with the headline text style.

`static let subheadline: Font`

A font with the subheadline text style.

`static let body: Font`

A font with the body text style.

`static let callout: Font`

A font with the callout text style.

`static let caption: Font`

A font with the caption text style.

`static let caption2: Font`

Create a font with the alternate caption text style.

`static let footnote: Font`

A font with the footnote text style.

Type Property

# title3

Create a font for third level hierarchical headings.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    static let title3: Font

## See Also

### Getting standard fonts

`static let extraLargeTitle2: Font`

Create a font with the second level extra large title text style.

`static let extraLargeTitle: Font`

Create a font with the extra large title text style.

`static let largeTitle: Font`

A font with the large title text style.

`static let title: Font`

A font with the title text style.

`static let title2: Font`

Create a font for second level hierarchical headings.

`static let headline: Font`

A font with the headline text style.

`static let subheadline: Font`

A font with the subheadline text style.

`static let body: Font`

A font with the body text style.

`static let callout: Font`

A font with the callout text style.

`static let caption: Font`

A font with the caption text style.

`static let caption2: Font`

Create a font with the alternate caption text style.

`static let footnote: Font`

A font with the footnote text style.

Type Property

# headline

A font with the headline text style.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static let headline: Font

## See Also

### Getting standard fonts

`static let extraLargeTitle2: Font`

Create a font with the second level extra large title text style.

`static let extraLargeTitle: Font`

Create a font with the extra large title text style.

`static let largeTitle: Font`

A font with the large title text style.

`static let title: Font`

A font with the title text style.

`static let title2: Font`

Create a font for second level hierarchical headings.

`static let title3: Font`

Create a font for third level hierarchical headings.

`static let subheadline: Font`

A font with the subheadline text style.

`static let body: Font`

A font with the body text style.

`static let callout: Font`

A font with the callout text style.

`static let caption: Font`

A font with the caption text style.

`static let caption2: Font`

Create a font with the alternate caption text style.

`static let footnote: Font`

A font with the footnote text style.

Type Property

# subheadline

A font with the subheadline text style.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static let subheadline: Font

## See Also

### Getting standard fonts

`static let extraLargeTitle2: Font`

Create a font with the second level extra large title text style.

`static let extraLargeTitle: Font`

Create a font with the extra large title text style.

`static let largeTitle: Font`

A font with the large title text style.

`static let title: Font`

A font with the title text style.

`static let title2: Font`

Create a font for second level hierarchical headings.

`static let title3: Font`

Create a font for third level hierarchical headings.

`static let headline: Font`

A font with the headline text style.

`static let body: Font`

A font with the body text style.

`static let callout: Font`

A font with the callout text style.

`static let caption: Font`

A font with the caption text style.

`static let caption2: Font`

Create a font with the alternate caption text style.

`static let footnote: Font`

A font with the footnote text style.

Type Property

# body

A font with the body text style.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static let body: Font

## See Also

### Getting standard fonts

`static let extraLargeTitle2: Font`

Create a font with the second level extra large title text style.

`static let extraLargeTitle: Font`

Create a font with the extra large title text style.

`static let largeTitle: Font`

A font with the large title text style.

`static let title: Font`

A font with the title text style.

`static let title2: Font`

Create a font for second level hierarchical headings.

`static let title3: Font`

Create a font for third level hierarchical headings.

`static let headline: Font`

A font with the headline text style.

`static let subheadline: Font`

A font with the subheadline text style.

`static let callout: Font`

A font with the callout text style.

`static let caption: Font`

A font with the caption text style.

`static let caption2: Font`

Create a font with the alternate caption text style.

`static let footnote: Font`

A font with the footnote text style.

Type Property

# callout

A font with the callout text style.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static let callout: Font

## See Also

### Getting standard fonts

`static let extraLargeTitle2: Font`

Create a font with the second level extra large title text style.

`static let extraLargeTitle: Font`

Create a font with the extra large title text style.

`static let largeTitle: Font`

A font with the large title text style.

`static let title: Font`

A font with the title text style.

`static let title2: Font`

Create a font for second level hierarchical headings.

`static let title3: Font`

Create a font for third level hierarchical headings.

`static let headline: Font`

A font with the headline text style.

`static let subheadline: Font`

A font with the subheadline text style.

`static let body: Font`

A font with the body text style.

`static let caption: Font`

A font with the caption text style.

`static let caption2: Font`

Create a font with the alternate caption text style.

`static let footnote: Font`

A font with the footnote text style.

Type Property

# caption

A font with the caption text style.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static let caption: Font

## See Also

### Getting standard fonts

`static let extraLargeTitle2: Font`

Create a font with the second level extra large title text style.

`static let extraLargeTitle: Font`

Create a font with the extra large title text style.

`static let largeTitle: Font`

A font with the large title text style.

`static let title: Font`

A font with the title text style.

`static let title2: Font`

Create a font for second level hierarchical headings.

`static let title3: Font`

Create a font for third level hierarchical headings.

`static let headline: Font`

A font with the headline text style.

`static let subheadline: Font`

A font with the subheadline text style.

`static let body: Font`

A font with the body text style.

`static let callout: Font`

A font with the callout text style.

`static let caption2: Font`

Create a font with the alternate caption text style.

`static let footnote: Font`

A font with the footnote text style.

Type Property

# caption2

Create a font with the alternate caption text style.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    static let caption2: Font

## See Also

### Getting standard fonts

`static let extraLargeTitle2: Font`

Create a font with the second level extra large title text style.

`static let extraLargeTitle: Font`

Create a font with the extra large title text style.

`static let largeTitle: Font`

A font with the large title text style.

`static let title: Font`

A font with the title text style.

`static let title2: Font`

Create a font for second level hierarchical headings.

`static let title3: Font`

Create a font for third level hierarchical headings.

`static let headline: Font`

A font with the headline text style.

`static let subheadline: Font`

A font with the subheadline text style.

`static let body: Font`

A font with the body text style.

`static let callout: Font`

A font with the callout text style.

`static let caption: Font`

A font with the caption text style.

`static let footnote: Font`

A font with the footnote text style.

Type Property

# footnote

A font with the footnote text style.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static let footnote: Font

## See Also

### Getting standard fonts

`static let extraLargeTitle2: Font`

Create a font with the second level extra large title text style.

`static let extraLargeTitle: Font`

Create a font with the extra large title text style.

`static let largeTitle: Font`

A font with the large title text style.

`static let title: Font`

A font with the title text style.

`static let title2: Font`

Create a font for second level hierarchical headings.

`static let title3: Font`

Create a font for third level hierarchical headings.

`static let headline: Font`

A font with the headline text style.

`static let subheadline: Font`

A font with the subheadline text style.

`static let body: Font`

A font with the body text style.

`static let callout: Font`

A font with the callout text style.

`static let caption: Font`

A font with the caption text style.

`static let caption2: Font`

Create a font with the alternate caption text style.

Type Method

# system(_:design:weight:)

Gets a system font that uses the specified style, design, and weight.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    static func system(
        _ style: Font.TextStyle,
        design: Font.Design? = nil,
        weight: Font.Weight? = nil
    ) -> Font

## Discussion

Use this method to create a system font that has the specified properties. The
following example creates a system font with the `Font.TextStyle.body` text
style, a `Font.Design.serif` design, and a `bold` weight, and applies the font
to a `Text` view using the `font(_:)` view modifier:

The `design` and `weight` parameters are both optional. If you omit either,
the system uses a default value for that parameter. The default values are
typically `Font.Design.default` and `regular`, respectively, but might vary
depending on the context.

## See Also

### Getting system fonts

`static func system(size: CGFloat, weight: Font.Weight?, design: Font.Design?)
-> Font`

Specifies a system font to use, along with the style, weight, and any design
parameters you want applied to the text.

`enum Design`

A design to use for fonts.

`enum TextStyle`

A dynamic text style to use for fonts.

`struct Weight`

A weight to use for fonts.

Type Method

# system(size:weight:design:)

Specifies a system font to use, along with the style, weight, and any design
parameters you want applied to the text.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    static func system(
        size: CGFloat,
        weight: Font.Weight? = nil,
        design: Font.Design? = nil
    ) -> Font

## Discussion

Use this function to create a system font by specifying the size and weight,
and a type design together. The following styles the system font as 17 point,
`semibold` text:

While the following styles the text as 17 point `bold`, and applies a `serif`
`Font.Design` to the system font:

Both `weight` and `design` can be optional. When you do not provide a `weight`
or `design`, the system can pick one based on the current context, which may
not be `regular` or `Font.Design.default` in certain context. The following
example styles the text as 17 point system font using `Font.Design.rounded`
design, while its weight can depend on the current context:

## See Also

### Getting system fonts

`static func system(Font.TextStyle, design: Font.Design?, weight:
Font.Weight?) -> Font`

Gets a system font that uses the specified style, design, and weight.

`enum Design`

A design to use for fonts.

`enum TextStyle`

A dynamic text style to use for fonts.

`struct Weight`

A weight to use for fonts.

Enumeration

# Font.Design

A design to use for fonts.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    enum Design

## Topics

### Getting font designs

`case `default``

`case monospaced`

`case rounded`

`case serif`

## Relationships

### Conforms To

  * `Equatable`
  * `Hashable`
  * `Sendable`

## See Also

### Getting system fonts

`static func system(Font.TextStyle, design: Font.Design?, weight:
Font.Weight?) -> Font`

Gets a system font that uses the specified style, design, and weight.

`static func system(size: CGFloat, weight: Font.Weight?, design: Font.Design?)
-> Font`

Specifies a system font to use, along with the style, weight, and any design
parameters you want applied to the text.

`enum TextStyle`

A dynamic text style to use for fonts.

`struct Weight`

A weight to use for fonts.

Enumeration

# Font.TextStyle

A dynamic text style to use for fonts.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    enum TextStyle

## Topics

### Getting font text styles

`case extraLargeTitle2`

The font used for second level extra large titles.

`case extraLargeTitle`

The font used for extra large titles.

`case largeTitle`

The font style for large titles.

`case title`

The font used for first level hierarchical headings.

`case title2`

The font used for second level hierarchical headings.

`case title3`

The font used for third level hierarchical headings.

`case headline`

The font used for headings.

`case subheadline`

The font used for subheadings.

`case body`

The font used for body text.

`case callout`

The font used for callouts.

`case caption`

The font used for standard captions.

`case caption2`

The font used for alternate captions.

`case footnote`

The font used in footnotes.

## Relationships

### Conforms To

  * `CaseIterable`
  * `Equatable`
  * `Hashable`
  * `Sendable`

## See Also

### Getting system fonts

`static func system(Font.TextStyle, design: Font.Design?, weight:
Font.Weight?) -> Font`

Gets a system font that uses the specified style, design, and weight.

`static func system(size: CGFloat, weight: Font.Weight?, design: Font.Design?)
-> Font`

Specifies a system font to use, along with the style, weight, and any design
parameters you want applied to the text.

`enum Design`

A design to use for fonts.

`struct Weight`

A weight to use for fonts.

Structure

# Font.Weight

A weight to use for fonts.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @frozen
    struct Weight

## Topics

### Getting font weights

`static let black: Font.Weight`

`static let bold: Font.Weight`

`static let heavy: Font.Weight`

`static let light: Font.Weight`

`static let medium: Font.Weight`

`static let regular: Font.Weight`

`static let semibold: Font.Weight`

`static let thin: Font.Weight`

`static let ultraLight: Font.Weight`

## Relationships

### Conforms To

  * `Equatable`
  * `Hashable`
  * `Sendable`

## See Also

### Getting system fonts

`static func system(Font.TextStyle, design: Font.Design?, weight:
Font.Weight?) -> Font`

Gets a system font that uses the specified style, design, and weight.

`static func system(size: CGFloat, weight: Font.Weight?, design: Font.Design?)
-> Font`

Specifies a system font to use, along with the style, weight, and any design
parameters you want applied to the text.

`enum Design`

A design to use for fonts.

`enum TextStyle`

A dynamic text style to use for fonts.

Type Method

# custom(_:fixedSize:)

Create a custom font with the given `name` and a fixed `size` that does not
scale with Dynamic Type.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    static func custom(
        _ name: String,
        fixedSize: CGFloat
    ) -> Font

## See Also

### Creating custom fonts

`static func custom(String, size: CGFloat, relativeTo: Font.TextStyle) ->
Font`

Create a custom font with the given `name` and `size` that scales relative to
the given `textStyle`.

`static func custom(String, size: CGFloat) -> Font`

Create a custom font with the given `name` and `size` that scales with the
body text style.

Type Method

# custom(_:size:relativeTo:)

Create a custom font with the given `name` and `size` that scales relative to
the given `textStyle`.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    static func custom(
        _ name: String,
        size: CGFloat,
        relativeTo textStyle: Font.TextStyle
    ) -> Font

## See Also

### Creating custom fonts

`static func custom(String, fixedSize: CGFloat) -> Font`

Create a custom font with the given `name` and a fixed `size` that does not
scale with Dynamic Type.

`static func custom(String, size: CGFloat) -> Font`

Create a custom font with the given `name` and `size` that scales with the
body text style.

Type Method

# custom(_:size:)

Create a custom font with the given `name` and `size` that scales with the
body text style.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static func custom(
        _ name: String,
        size: CGFloat
    ) -> Font

## See Also

### Creating custom fonts

`static func custom(String, fixedSize: CGFloat) -> Font`

Create a custom font with the given `name` and a fixed `size` that does not
scale with Dynamic Type.

`static func custom(String, size: CGFloat, relativeTo: Font.TextStyle) ->
Font`

Create a custom font with the given `name` and `size` that scales relative to
the given `textStyle`.

Initializer

# init(_:)

Creates a custom font from a platform font instance.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init(_ font: CTFont)

## Discussion

Initializing `Font` with platform font instance (CTFont) can bridge SwiftUI
`Font` with `NSFont` or `UIFont`, both of which are toll-free bridged to
CTFont. For example:

Instance Method

# bold()

Adds bold styling to the font.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func bold() -> Font

## See Also

### Styling a font

`func italic() -> Font`

Adds italics to the font.

`func monospaced() -> Font`

Returns a fixed-width font from the same family as the base font.

`func monospacedDigit() -> Font`

Returns a modified font that uses fixed-width digits, while leaving other
characters proportionally spaced.

`func smallCaps() -> Font`

Adjusts the font to enable all small capitals.

`func lowercaseSmallCaps() -> Font`

Adjusts the font to enable lowercase small capitals.

`func uppercaseSmallCaps() -> Font`

Adjusts the font to enable uppercase small capitals.

`func weight(Font.Weight) -> Font`

Sets the weight of the font.

`func width(Font.Width) -> Font`

Sets the width of the font.

`struct Width`

A width to use for fonts that have multiple widths.

`func leading(Font.Leading) -> Font`

Adjusts the line spacing of a font.

`enum Leading`

A line spacing adjustment that you can apply to a font.

Instance Method

# italic()

Adds italics to the font.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func italic() -> Font

## See Also

### Styling a font

`func bold() -> Font`

Adds bold styling to the font.

`func monospaced() -> Font`

Returns a fixed-width font from the same family as the base font.

`func monospacedDigit() -> Font`

Returns a modified font that uses fixed-width digits, while leaving other
characters proportionally spaced.

`func smallCaps() -> Font`

Adjusts the font to enable all small capitals.

`func lowercaseSmallCaps() -> Font`

Adjusts the font to enable lowercase small capitals.

`func uppercaseSmallCaps() -> Font`

Adjusts the font to enable uppercase small capitals.

`func weight(Font.Weight) -> Font`

Sets the weight of the font.

`func width(Font.Width) -> Font`

Sets the width of the font.

`struct Width`

A width to use for fonts that have multiple widths.

`func leading(Font.Leading) -> Font`

Adjusts the line spacing of a font.

`enum Leading`

A line spacing adjustment that you can apply to a font.

Instance Method

# monospaced()

Returns a fixed-width font from the same family as the base font.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func monospaced() -> Font

## Return Value

A fixed-width font from the same family as the base font, if one is available,
and a default fixed-width font otherwise.

## Discussion

If there’s no suitable font face in the same family, SwiftUI returns a default
fixed-width font.

The following example adds the `monospaced()` modifier to the default system
font, then applies this font to a `Text` view:

SwiftUI may provide different fixed-width replacements for standard user
interface fonts (such as `title`, or a system font created with
`system(_:design:)`) than for those same fonts when created by name with
`custom(_:size:)`.

The `font(_:)` modifier applies the font to all text within the view. To mix
fixed-width text with other styles in the same `Text` view, use the `init(_:)`
initializer to use an appropropriately-styled `AttributedString` for the text
view’s content. You can use the `init(markdown:options:baseURL:)` initializer
to provide a Markdown-formatted string containing the backtick-syntax (`…`) to
apply code voice to specific ranges of the attributed string.

## See Also

### Styling a font

`func bold() -> Font`

Adds bold styling to the font.

`func italic() -> Font`

Adds italics to the font.

`func monospacedDigit() -> Font`

Returns a modified font that uses fixed-width digits, while leaving other
characters proportionally spaced.

`func smallCaps() -> Font`

Adjusts the font to enable all small capitals.

`func lowercaseSmallCaps() -> Font`

Adjusts the font to enable lowercase small capitals.

`func uppercaseSmallCaps() -> Font`

Adjusts the font to enable uppercase small capitals.

`func weight(Font.Weight) -> Font`

Sets the weight of the font.

`func width(Font.Width) -> Font`

Sets the width of the font.

`struct Width`

A width to use for fonts that have multiple widths.

`func leading(Font.Leading) -> Font`

Adjusts the line spacing of a font.

`enum Leading`

A line spacing adjustment that you can apply to a font.

Instance Method

# monospacedDigit()

Returns a modified font that uses fixed-width digits, while leaving other
characters proportionally spaced.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func monospacedDigit() -> Font

## Return Value

A font that uses fixed-width numeric characters.

## Discussion

This modifier only affects numeric characters, and leaves all other characters
unchanged. If the base font doesn’t support fixed-width, or _monospace_
digits, the font remains unchanged.

The following example shows two text fields arranged in a `VStack`. Both text
fields specify the 12-point system font, with the second adding the
`monospacedDigit()` modifier to the font. Because the text includes the digit
1, normally a narrow character in proportional fonts, the second text field
becomes wider than the first.

## See Also

### Styling a font

`func bold() -> Font`

Adds bold styling to the font.

`func italic() -> Font`

Adds italics to the font.

`func monospaced() -> Font`

Returns a fixed-width font from the same family as the base font.

`func smallCaps() -> Font`

Adjusts the font to enable all small capitals.

`func lowercaseSmallCaps() -> Font`

Adjusts the font to enable lowercase small capitals.

`func uppercaseSmallCaps() -> Font`

Adjusts the font to enable uppercase small capitals.

`func weight(Font.Weight) -> Font`

Sets the weight of the font.

`func width(Font.Width) -> Font`

Sets the width of the font.

`struct Width`

A width to use for fonts that have multiple widths.

`func leading(Font.Leading) -> Font`

Adjusts the line spacing of a font.

`enum Leading`

A line spacing adjustment that you can apply to a font.

Instance Method

# smallCaps()

Adjusts the font to enable all small capitals.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func smallCaps() -> Font

## Discussion

See `lowercaseSmallCaps()` and `uppercaseSmallCaps()` for more details.

## See Also

### Styling a font

`func bold() -> Font`

Adds bold styling to the font.

`func italic() -> Font`

Adds italics to the font.

`func monospaced() -> Font`

Returns a fixed-width font from the same family as the base font.

`func monospacedDigit() -> Font`

Returns a modified font that uses fixed-width digits, while leaving other
characters proportionally spaced.

`func lowercaseSmallCaps() -> Font`

Adjusts the font to enable lowercase small capitals.

`func uppercaseSmallCaps() -> Font`

Adjusts the font to enable uppercase small capitals.

`func weight(Font.Weight) -> Font`

Sets the weight of the font.

`func width(Font.Width) -> Font`

Sets the width of the font.

`struct Width`

A width to use for fonts that have multiple widths.

`func leading(Font.Leading) -> Font`

Adjusts the line spacing of a font.

`enum Leading`

A line spacing adjustment that you can apply to a font.

Instance Method

# lowercaseSmallCaps()

Adjusts the font to enable lowercase small capitals.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func lowercaseSmallCaps() -> Font

## Discussion

This function turns lowercase characters into small capitals for the font. It
is generally used for display lines set in large and small caps, such as
titles. It may include forms related to small capitals, such as old-style
figures.

## See Also

### Styling a font

`func bold() -> Font`

Adds bold styling to the font.

`func italic() -> Font`

Adds italics to the font.

`func monospaced() -> Font`

Returns a fixed-width font from the same family as the base font.

`func monospacedDigit() -> Font`

Returns a modified font that uses fixed-width digits, while leaving other
characters proportionally spaced.

`func smallCaps() -> Font`

Adjusts the font to enable all small capitals.

`func uppercaseSmallCaps() -> Font`

Adjusts the font to enable uppercase small capitals.

`func weight(Font.Weight) -> Font`

Sets the weight of the font.

`func width(Font.Width) -> Font`

Sets the width of the font.

`struct Width`

A width to use for fonts that have multiple widths.

`func leading(Font.Leading) -> Font`

Adjusts the line spacing of a font.

`enum Leading`

A line spacing adjustment that you can apply to a font.

Instance Method

# uppercaseSmallCaps()

Adjusts the font to enable uppercase small capitals.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func uppercaseSmallCaps() -> Font

## Discussion

This feature turns capital characters into small capitals. It is generally
used for words which would otherwise be set in all caps, such as acronyms, but
which are desired in small-cap form to avoid disrupting the flow of text.

## See Also

### Styling a font

`func bold() -> Font`

Adds bold styling to the font.

`func italic() -> Font`

Adds italics to the font.

`func monospaced() -> Font`

Returns a fixed-width font from the same family as the base font.

`func monospacedDigit() -> Font`

Returns a modified font that uses fixed-width digits, while leaving other
characters proportionally spaced.

`func smallCaps() -> Font`

Adjusts the font to enable all small capitals.

`func lowercaseSmallCaps() -> Font`

Adjusts the font to enable lowercase small capitals.

`func weight(Font.Weight) -> Font`

Sets the weight of the font.

`func width(Font.Width) -> Font`

Sets the width of the font.

`struct Width`

A width to use for fonts that have multiple widths.

`func leading(Font.Leading) -> Font`

Adjusts the line spacing of a font.

`enum Leading`

A line spacing adjustment that you can apply to a font.

Instance Method

# weight(_:)

Sets the weight of the font.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func weight(_ weight: Font.Weight) -> Font

## See Also

### Styling a font

`func bold() -> Font`

Adds bold styling to the font.

`func italic() -> Font`

Adds italics to the font.

`func monospaced() -> Font`

Returns a fixed-width font from the same family as the base font.

`func monospacedDigit() -> Font`

Returns a modified font that uses fixed-width digits, while leaving other
characters proportionally spaced.

`func smallCaps() -> Font`

Adjusts the font to enable all small capitals.

`func lowercaseSmallCaps() -> Font`

Adjusts the font to enable lowercase small capitals.

`func uppercaseSmallCaps() -> Font`

Adjusts the font to enable uppercase small capitals.

`func width(Font.Width) -> Font`

Sets the width of the font.

`struct Width`

A width to use for fonts that have multiple widths.

`func leading(Font.Leading) -> Font`

Adjusts the line spacing of a font.

`enum Leading`

A line spacing adjustment that you can apply to a font.

Instance Method

# width(_:)

Sets the width of the font.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func width(_ width: Font.Width) -> Font

## See Also

### Styling a font

`func bold() -> Font`

Adds bold styling to the font.

`func italic() -> Font`

Adds italics to the font.

`func monospaced() -> Font`

Returns a fixed-width font from the same family as the base font.

`func monospacedDigit() -> Font`

Returns a modified font that uses fixed-width digits, while leaving other
characters proportionally spaced.

`func smallCaps() -> Font`

Adjusts the font to enable all small capitals.

`func lowercaseSmallCaps() -> Font`

Adjusts the font to enable lowercase small capitals.

`func uppercaseSmallCaps() -> Font`

Adjusts the font to enable uppercase small capitals.

`func weight(Font.Weight) -> Font`

Sets the weight of the font.

`struct Width`

A width to use for fonts that have multiple widths.

`func leading(Font.Leading) -> Font`

Adjusts the line spacing of a font.

`enum Leading`

A line spacing adjustment that you can apply to a font.

Structure

# Font.Width

A width to use for fonts that have multiple widths.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    struct Width

## Topics

### Getting standard font widths

`static let compressed: Font.Width`

`static let condensed: Font.Width`

`static let expanded: Font.Width`

`static let standard: Font.Width`

### Creating an explicit font width

`init(CGFloat)`

### Accessing the width’s value

`var value: CGFloat`

## Relationships

### Conforms To

  * `Equatable`
  * `Hashable`
  * `Sendable`

## See Also

### Styling a font

`func bold() -> Font`

Adds bold styling to the font.

`func italic() -> Font`

Adds italics to the font.

`func monospaced() -> Font`

Returns a fixed-width font from the same family as the base font.

`func monospacedDigit() -> Font`

Returns a modified font that uses fixed-width digits, while leaving other
characters proportionally spaced.

`func smallCaps() -> Font`

Adjusts the font to enable all small capitals.

`func lowercaseSmallCaps() -> Font`

Adjusts the font to enable lowercase small capitals.

`func uppercaseSmallCaps() -> Font`

Adjusts the font to enable uppercase small capitals.

`func weight(Font.Weight) -> Font`

Sets the weight of the font.

`func width(Font.Width) -> Font`

Sets the width of the font.

`func leading(Font.Leading) -> Font`

Adjusts the line spacing of a font.

`enum Leading`

A line spacing adjustment that you can apply to a font.

Instance Method

# leading(_:)

Adjusts the line spacing of a font.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    func leading(_ leading: Font.Leading) -> Font

##  Parameters

`leading`

    

The line spacing adjustment to apply.

## Return Value

A modified font that uses the specified line spacing, or the original font if
it doesn’t support line spacing adjustments.

## Discussion

You can change a font’s line spacing while maintaining other characteristics
of the font by applying this modifier. For example, you can decrease spacing
of the `body` font by applying the `Font.Leading.tight` value to it:

The availability of leading adjustments depends on the font. For some fonts,
the modifier has no effect and returns the original font.

## See Also

### Styling a font

`func bold() -> Font`

Adds bold styling to the font.

`func italic() -> Font`

Adds italics to the font.

`func monospaced() -> Font`

Returns a fixed-width font from the same family as the base font.

`func monospacedDigit() -> Font`

Returns a modified font that uses fixed-width digits, while leaving other
characters proportionally spaced.

`func smallCaps() -> Font`

Adjusts the font to enable all small capitals.

`func lowercaseSmallCaps() -> Font`

Adjusts the font to enable lowercase small capitals.

`func uppercaseSmallCaps() -> Font`

Adjusts the font to enable uppercase small capitals.

`func weight(Font.Weight) -> Font`

Sets the weight of the font.

`func width(Font.Width) -> Font`

Sets the width of the font.

`struct Width`

A width to use for fonts that have multiple widths.

`enum Leading`

A line spacing adjustment that you can apply to a font.

Enumeration

# Font.Leading

A line spacing adjustment that you can apply to a font.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    enum Leading

## Overview

Apply one of the `Leading` values to a font using the `leading(_:)` method to
increase or decrease the line spacing.

## Topics

### Getting leading line spacing options

`case standard`

The font’s default line spacing.

`case loose`

Increased line spacing.

`case tight`

Reduced line spacing.

## Relationships

### Conforms To

  * `Equatable`
  * `Hashable`
  * `Sendable`

## See Also

### Styling a font

`func bold() -> Font`

Adds bold styling to the font.

`func italic() -> Font`

Adds italics to the font.

`func monospaced() -> Font`

Returns a fixed-width font from the same family as the base font.

`func monospacedDigit() -> Font`

Returns a modified font that uses fixed-width digits, while leaving other
characters proportionally spaced.

`func smallCaps() -> Font`

Adjusts the font to enable all small capitals.

`func lowercaseSmallCaps() -> Font`

Adjusts the font to enable lowercase small capitals.

`func uppercaseSmallCaps() -> Font`

Adjusts the font to enable uppercase small capitals.

`func weight(Font.Weight) -> Font`

Sets the weight of the font.

`func width(Font.Width) -> Font`

Sets the width of the font.

`struct Width`

A width to use for fonts that have multiple widths.

`func leading(Font.Leading) -> Font`

Adjusts the line spacing of a font.

Type Method

# system(_:design:)

Gets a system font with the given text style and design.

iOS 13.0–17.4  Deprecated  iPadOS 13.0–17.4  Deprecated  macOS 10.15–14.4
Deprecated  Mac Catalyst 13.0–17.4  Deprecated  tvOS 13.0–17.4  Deprecated
watchOS 6.0–10.4  Deprecated  visionOS 1.0+

    
    
    static func system(
        _ style: Font.TextStyle,
        design: Font.Design = .default
    ) -> Font

Deprecated

Use `system(_:design:weight:)` instead.

## See Also

### Deprecated symbols

`static func system(size: CGFloat, weight: Font.Weight, design: Font.Design)
-> Font`

Specifies a system font to use, along with the style, weight, and any design
parameters you want applied to the text.

Deprecated

Type Method

# system(size:weight:design:)

Specifies a system font to use, along with the style, weight, and any design
parameters you want applied to the text.

iOS 13.0–17.4  Deprecated  iPadOS 13.0–17.4  Deprecated  macOS 10.15–14.4
Deprecated  Mac Catalyst 13.0–17.4  Deprecated  tvOS 13.0–17.4  Deprecated
watchOS 6.0–10.4  Deprecated  visionOS 1.0+

    
    
    static func system(
        size: CGFloat,
        weight: Font.Weight = .regular,
        design: Font.Design = .default
    ) -> Font

Deprecated

Use `system(size:weight:design:)` instead.

## Discussion

Use this function to create a system font by specifying the size and weight,
and a type design together. The following styles the system font as 17 point,
`semibold` text:

While the following styles the text as 17 point `bold`, and applies a `serif`
`Font.Design` to the system font:

If you want to use the default `Font.Weight` (`regular`), you don’t need to
specify the `weight` in the method. The following example styles the text as
17 point `regular`, and uses a `Font.Design.rounded` system font:

## See Also

### Deprecated symbols

`static func system(Font.TextStyle, design: Font.Design) -> Font`

Gets a system font with the given text style and design.

Deprecated



# FocusedValueKey

Associated Type

# Value

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    associatedtype Value

**Required**



# FocusedObject.Wrapper

Instance Subscript

# subscript(dynamicMember:)

Returns a binding to the value of a given key path.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    subscript<T>(dynamicMember keyPath: ReferenceWritableKeyPath<ObjectType, T>) -> Binding<T> { get }

##  Parameters

`keyPath`

    

A key path to a specific value on the wrapped object.

## Return Value

A new binding.



# FetchRequest

Initializer

# init(sortDescriptors:predicate:animation:)

Creates a fetch request based on a predicate and value type sort parameters.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    @MainActor
    init(
        sortDescriptors: [SortDescriptor<Result>],
        predicate: NSPredicate? = nil,
        animation: Animation? = nil
    )

Available when `Result` inherits `NSManagedObject`.

##  Parameters

`sortDescriptors`

    

An array of sort descriptors that define the sort order of the fetched
results.

`predicate`

    

An `NSPredicate` instance that defines logical conditions used to filter the
fetched results.

`animation`

    

The animation to use for user interface changes that result from changes to
the fetched results.

## Discussion

The request gets the entity type from the `Result` instance by calling that
managed object’s `entity()` type method. If you need to specify the entity
type explicitly, use the `init(entity:sortDescriptors:predicate:animation:)`
initializer instead. If you need more control over the fetch request
configuration, use `init(fetchRequest:animation:)`. For reference type sort
descriptors, use `init(sortDescriptors:predicate:animation:)`.

## See Also

### Creating a fetch request

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

Initializer

# init(sortDescriptors:predicate:animation:)

Creates a fetch request based on a predicate and reference type sort
parameters.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @MainActor
    init(
        sortDescriptors: [NSSortDescriptor],
        predicate: NSPredicate? = nil,
        animation: Animation? = nil
    )

Available when `Result` inherits `NSManagedObject`.

##  Parameters

`sortDescriptors`

    

An array of sort descriptors that define the sort order of the fetched
results.

`predicate`

    

An `NSPredicate` instance that defines logical conditions used to filter the
fetched results.

`animation`

    

The animation to use for user interface changes that result from changes to
the fetched results.

## Discussion

The request gets the entity type from the `Result` instance by calling that
managed object’s `entity()` type method. If you need to specify the entity
type explicitly, use the `init(entity:sortDescriptors:predicate:animation:)`
initializer instead. If you need more control over the fetch request
configuration, use `init(fetchRequest:animation:)`. For value type sort
descriptors, use `init(sortDescriptors:predicate:animation:)`.

## See Also

### Creating a fetch request

`init(sortDescriptors: [SortDescriptor<Result>], predicate: NSPredicate?,
animation: Animation?)`

Creates a fetch request based on a predicate and value type sort parameters.

Available when `Result` inherits `NSManagedObject`.

`init(entity: NSEntityDescription, sortDescriptors: [NSSortDescriptor],
predicate: NSPredicate?, animation: Animation?)`

Creates a fetch request for a specified entity description, based on a
predicate and sort parameters.

Available when `Result` conforms to `NSFetchRequestResult`.

Initializer

# init(entity:sortDescriptors:predicate:animation:)

Creates a fetch request for a specified entity description, based on a
predicate and sort parameters.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @MainActor
    init(
        entity: NSEntityDescription,
        sortDescriptors: [NSSortDescriptor],
        predicate: NSPredicate? = nil,
        animation: Animation? = nil
    )

Available when `Result` conforms to `NSFetchRequestResult`.

##  Parameters

`entity`

    

The description of the Core Data entity to fetch.

`sortDescriptors`

    

An array of sort descriptors that define the sort order of the fetched
results.

`predicate`

    

An `NSPredicate` instance that defines logical conditions used to filter the
fetched results.

`animation`

    

The animation to use for user interface changes that result from changes to
the fetched results.

## Discussion

Use this initializer if you need to explicitly specify the entity type for the
request. If you specify a placeholder `Result` type in the request
declaration, use the `init(sortDescriptors:predicate:animation:)` initializer
to let the request infer the entity type. If you need more control over the
fetch request configuration, use `init(fetchRequest:animation:)`.

## See Also

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

Initializer

# init(fetchRequest:animation:)

Creates a fully configured fetch request that uses the specified animation
when updating results.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @MainActor
    init(
        fetchRequest: NSFetchRequest<Result>,
        animation: Animation? = nil
    )

Available when `Result` conforms to `NSFetchRequestResult`.

##  Parameters

`fetchRequest`

    

An `NSFetchRequest` instance that describes the search criteria for retrieving
data from the persistent store.

`animation`

    

The animation to use for user interface changes that result from changes to
the fetched results.

## Discussion

Use this initializer when you want to configure a fetch request with more than
a predicate and sort descriptors. For example, you can vend a request from a
`Quake` managed object that the Loading and Displaying a Large Data Feed
sample code project defines to store earthquake data. Limit the number of
results to `1000` by setting a `fetchLimit` for the request:

Use the request to define a `FetchedResults` property:

If you only need to configure the request’s predicate and sort descriptors,
use `init(sortDescriptors:predicate:animation:)` instead. If you need to
specify a `Transaction` rather than an optional `Animation`, use
`init(fetchRequest:transaction:)`.

## See Also

### Creating a fully configured fetch request

`init(fetchRequest: NSFetchRequest<Result>, transaction: Transaction)`

Creates a fully configured fetch request that uses the specified transaction
when updating results.

Available when `Result` conforms to `NSFetchRequestResult`.

Initializer

# init(fetchRequest:transaction:)

Creates a fully configured fetch request that uses the specified transaction
when updating results.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @MainActor
    init(
        fetchRequest: NSFetchRequest<Result>,
        transaction: Transaction
    )

Available when `Result` conforms to `NSFetchRequestResult`.

##  Parameters

`fetchRequest`

    

An `NSFetchRequest` instance that describes the search criteria for retrieving
data from the persistent store.

`transaction`

    

A transaction to use for user interface changes that result from changes to
the fetched results.

## Discussion

Use this initializer if you need a fetch request with updates that affect the
user interface based on a `Transaction`. Otherwise, use
`init(fetchRequest:animation:)`.

## See Also

### Creating a fully configured fetch request

`init(fetchRequest: NSFetchRequest<Result>, animation: Animation?)`

Creates a fully configured fetch request that uses the specified animation
when updating results.

Available when `Result` conforms to `NSFetchRequestResult`.

Structure

# FetchRequest.Configuration

The request’s configurable properties.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    struct Configuration

## Overview

You initialize a `FetchRequest` with an optional predicate and sort
descriptors, either explicitly or using a configured `NSFetchRequest`. Later,
you can dynamically update the predicate and sort parameters using the
request’s configuration structure.

You access or bind to a request’s configuration components through properties
on the associated `FetchedResults` instance.

### Configure using a binding

Get a `Binding` to a fetch request’s configuration structure by accessing the
request’s `projectedValue`, which you do by using the dollar sign (`$`) prefix
on the associated results property. For example, you can create a request for
`Quake` entities — a managed object type that the Loading and Displaying a
Large Data Feed sample code project defines — that initially sorts the results
by time:

Then you can bind the request’s sort descriptors, which you access through the
`quakes` result, to those of a `Table` instance:

A user who clicks on a table column header initiates the following sequence of
events:

  1. The table updates the sort descriptors through the binding.

  2. The modified sort descriptors reconfigure the request.

  3. The reconfigured request fetches new results.

  4. SwiftUI redraws the table in response to new results.

### Set configuration directly

If you need to access the fetch request’s configuration elements directly, use
the `nsPredicate` and `sortDescriptors` or `nsSortDescriptors` properties of
the `FetchedResults` instance. Continuing the example above, to enable the
user to dynamically update the predicate, declare a `State` property to hold a
query string:

Then add an `onChange(of:initial:_:)` modifier to the `Table` that sets a new
predicate any time the query changes:

To give the user control over the string, add a `TextField` in your user
interface that’s bound to the `query` state:

When the user types into the text field, the predicate updates, the request
fetches new results, and SwiftUI redraws the table.

## Topics

### Setting a predicate

`var nsPredicate: NSPredicate?`

The request’s predicate.

### Setting sort descriptors

`var sortDescriptors: [SortDescriptor<Result>]`

The request’s sort descriptors, accessed as value types.

Available when `Result` inherits `NSManagedObject`.

`var nsSortDescriptors: [NSSortDescriptor]`

The request’s sort descriptors, accessed as reference types.

## See Also

### Configuring a request dynamically

`var projectedValue: Binding<FetchRequest<Result>.Configuration>`

A binding to the request’s mutable configuration properties.

Instance Property

# projectedValue

A binding to the request’s mutable configuration properties.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    @MainActor
    var projectedValue: Binding<FetchRequest<Result>.Configuration> { get }

## Discussion

SwiftUI returns the value associated with this property when you use
`FetchRequest` as a property wrapper on a `FetchedResults` instance, and then
access the results with a dollar sign (`$`) prefix. The value that SwiftUI
returns is a `Binding` to the request’s `FetchRequest.Configuration`
structure, which dynamically configures the request.

For example, consider the following fetch request for a type that the Loading
and Displaying a Large Data Feed sample code project defines to store
earthquake data, sorted based on the `time` property:

You can use the projected value to enable a `Table` instance to make updates:

Because you initialize the table using a binding to the descriptors, the table
can modify the sort in response to actions that the user takes, like clicking
a column header.

## See Also

### Configuring a request dynamically

`struct Configuration`

The request’s configurable properties.

Instance Method

# update()

Updates the fetched results.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @MainActor
    mutating func update()

Available when `Result` conforms to `NSFetchRequestResult`.

## Discussion

SwiftUI calls this function before rendering a view’s `body` to ensure the
view has the most recent fetched results.

## See Also

### Getting the fetched results

`var wrappedValue: FetchedResults<Result>`

The fetched results of the fetch request.

Instance Property

# wrappedValue

The fetched results of the fetch request.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @MainActor
    var wrappedValue: FetchedResults<Result> { get }

## Discussion

SwiftUI returns the value associated with this property when you use
`FetchRequest` as a property wrapper, and then access the wrapped property by
name. For example, consider the following `quakes` property declaration that
fetches a `Quake` type that the Loading and Displaying a Large Data Feed
sample code project defines:

You access the request’s `wrappedValue`, which contains a `FetchedResults`
instance, by referring to the `quakes` property by name:

If you need to separate the request and the result entities, you can declare
`quakes` in two steps by using the request’s `wrappedValue` to obtain the
results:

The `wrappedValue` property returns an empty array when there are no fetched
results — for example, because no entities satisfy the predicate, or because
the data store is empty.

## See Also

### Getting the fetched results

`func update()`

Updates the fetched results.

Available when `Result` conforms to `NSFetchRequestResult`.

Collection

API Collection

# DynamicProperty Implementations

## Topics

### Instance Methods

`func update()`

Updates the fetched results.

Available when `Result` conforms to `NSFetchRequestResult`.



# FocusState.Binding

Instance Property

# projectedValue

A projection of the binding value that returns a binding.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    var projectedValue: FocusState<Value>.Binding { get }

## Discussion

Use the projected value to pass a binding value down a view hierarchy.

## See Also

### Inspecting the binding

`var wrappedValue: Value`

The underlying value referenced by the bound property.

Instance Property

# wrappedValue

The underlying value referenced by the bound property.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    var wrappedValue: Value { get nonmutating set }

## See Also

### Inspecting the binding

`var projectedValue: FocusState<Value>.Binding`

A projection of the binding value that returns a binding.



# FillShapeStyle

Initializer

# init()

An overlay fill style for filling shapes.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    init()

## Discussion

This shape style is appropriate for items situated on top of an existing
background color. It incorporates transparency to allow the background color
to show through.

Use the primary version of this style to fill thin or small shapes, such as
the track of a slider. Use the secondary version of this style to fill medium-
size shapes, such as the background of a switch. Use the tertiary version of
this style to fill large shapes, such as input fields, search bars, or
buttons. Use the quaternary version of this style to fill large areas that
contain complex content, such as an expanded table cell.



# FileDocumentWriteConfiguration

Instance Property

# contentType

The expected uniform type of the file contents.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    let contentType: UTType

## See Also

### Writing the content

`let existingFile: FileWrapper?`

The file wrapper containing the current document content. `nil` if the
document is unsaved.

Instance Property

# existingFile

The file wrapper containing the current document content. `nil` if the
document is unsaved.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    let existingFile: FileWrapper?

## See Also

### Writing the content

`let contentType: UTType`

The expected uniform type of the file contents.



# FileDocumentReadConfiguration

Instance Property

# contentType

The expected uniform type of the file contents.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    let contentType: UTType

## See Also

### Reading the content

`let file: FileWrapper`

The file wrapper containing the document content.

Instance Property

# file

The file wrapper containing the document content.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    let file: FileWrapper

## See Also

### Reading the content

`let contentType: UTType`

The expected uniform type of the file contents.



