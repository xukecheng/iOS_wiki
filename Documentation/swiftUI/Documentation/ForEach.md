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

