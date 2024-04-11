# OpenURLAction.Result

Type Property

# discarded

The handler discarded the URL.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static let discarded: OpenURLAction.Result

## Discussion

The action invokes its completion handler with `false` when your handler
returns this value.

## See Also

### Getting the results

`static let handled: OpenURLAction.Result`

The handler opened the URL.

`static let systemAction: OpenURLAction.Result`

The handler asks the system to open the original URL.

`static func systemAction(URL) -> OpenURLAction.Result`

The handler asks the system to open the modified URL.

Type Property

# handled

The handler opened the URL.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static let handled: OpenURLAction.Result

## Discussion

The action invokes its completion handler with `true` when your handler
returns this value.

## See Also

### Getting the results

`static let discarded: OpenURLAction.Result`

The handler discarded the URL.

`static let systemAction: OpenURLAction.Result`

The handler asks the system to open the original URL.

`static func systemAction(URL) -> OpenURLAction.Result`

The handler asks the system to open the modified URL.

Type Property

# systemAction

The handler asks the system to open the original URL.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static let systemAction: OpenURLAction.Result

## Discussion

The action invokes its completion handler with a value that depends on the
outcome of the system’s attempt to open the URL.

## See Also

### Getting the results

`static let discarded: OpenURLAction.Result`

The handler discarded the URL.

`static let handled: OpenURLAction.Result`

The handler opened the URL.

`static func systemAction(URL) -> OpenURLAction.Result`

The handler asks the system to open the modified URL.

Type Method

# systemAction(_:)

The handler asks the system to open the modified URL.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static func systemAction(_ url: URL) -> OpenURLAction.Result

##  Parameters

`url`

    

The URL that the handler asks the system to open.

## Discussion

The action invokes its completion handler with a value that depends on the
outcome of the system’s attempt to open the URL.

## See Also

### Getting the results

`static let discarded: OpenURLAction.Result`

The handler discarded the URL.

`static let handled: OpenURLAction.Result`

The handler opened the URL.

`static let systemAction: OpenURLAction.Result`

The handler asks the system to open the original URL.



# ObservedObject

Initializer

# init(wrappedValue:)

Creates an observed object with an initial wrapped value.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init(wrappedValue: ObjectType)

##  Parameters

`wrappedValue`

    

An initial value for the observable object.

## Discussion

Don’t call this initializer directly. Instead, declare an input to a view with
the `@ObservedObject` attribute, and pass a value to this input when you
instantiate the view. Unlike a `StateObject` which manages data storage, you
use an observed object to refer to storage that you manage elsewhere, as in
the following example:

Explicitly calling the observed object initializer in `MySubView` would behave
correctly, but would needlessly recreate the same observed object instance
every time SwiftUI calls the view’s initializer to redraw the view.

## See Also

### Creating an observed object

`init(initialValue: ObjectType)`

Creates an observed object with an initial value.

Initializer

# init(initialValue:)

Creates an observed object with an initial value.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init(initialValue: ObjectType)

##  Parameters

`initialValue`

    

An initial value.

## Discussion

This initializer has the same behavior as the `init(wrappedValue:)`
initializer. See that initializer for more information.

## See Also

### Creating an observed object

`init(wrappedValue: ObjectType)`

Creates an observed object with an initial wrapped value.

Instance Property

# wrappedValue

The underlying value that the observed object references.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @MainActor
    var wrappedValue: ObjectType

## Discussion

The wrapped value property provides primary access to the observed object’s
data. However, you don’t typically access it by name. Instead, SwiftUI
accesses this property for you when you refer to the variable that you create
with the `@ObservedObject` attribute.

When you change a wrapped value, you can access the new value immediately.
However, SwiftUI updates views that display the value asynchronously, so the
interface might not update immediately.

## See Also

### Getting the value

`var projectedValue: ObservedObject<ObjectType>.Wrapper`

A projection of the observed object that creates bindings to its properties.

`struct Wrapper`

A wrapper of the underlying observable object that can create bindings to its
properties.

Instance Property

# projectedValue

A projection of the observed object that creates bindings to its properties.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @MainActor
    var projectedValue: ObservedObject<ObjectType>.Wrapper { get }

## Discussion

Use the projected value to get a `Binding` to a property of an observed
object. To access the projected value, prefix the property variable with a
dollar sign (`$`). For example, you can get a binding to a model’s `isEnabled`
Boolean so that a `Toggle` can control its value:

## See Also

### Getting the value

`var wrappedValue: ObjectType`

The underlying value that the observed object references.

`struct Wrapper`

A wrapper of the underlying observable object that can create bindings to its
properties.

Structure

# ObservedObject.Wrapper

A wrapper of the underlying observable object that can create bindings to its
properties.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @dynamicMemberLookup @frozen
    struct Wrapper

## Topics

### Subscripts

`subscript<Subject>(dynamicMember _: ReferenceWritableKeyPath<ObjectType,
Subject>) -> Binding<Subject>`

Gets a binding to the value of a specified key path.

## See Also

### Getting the value

`var wrappedValue: ObjectType`

The underlying value that the observed object references.

`var projectedValue: ObservedObject<ObjectType>.Wrapper`

A projection of the observed object that creates bindings to its properties.



# ObservedObject.Wrapper

Instance Subscript

# subscript(dynamicMember:)

Gets a binding to the value of a specified key path.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    subscript<Subject>(dynamicMember keyPath: ReferenceWritableKeyPath<ObjectType, Subject>) -> Binding<Subject> { get }

##  Parameters

`keyPath`

    

A key path to a specific value.

## Return Value

A new binding.



# OpacityTransition

Initializer

# init()

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    init()



# OutlineGroup

Initializer

# init(_:children:content:)

Creates an outline group from a root data element and a key path to its
children.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    init<DataElement>(
        _ root: DataElement,
        children: KeyPath<DataElement, Data?>,
        @ViewBuilder content: @escaping (DataElement) -> Leaf
    ) where ID == DataElement.ID, DataElement : Identifiable, DataElement == Data.Element

Available when `Data` conforms to `RandomAccessCollection`, `ID` is
`Data.Element.ID`, `Parent` conforms to `View`, `Parent` is `Leaf`, `Subgroup`
is `DisclosureGroup<Parent, OutlineSubgroupChildren>`, and `Data.Element`
conforms to `Identifiable`.

##  Parameters

`root`

    

The root of a collection of tree-structured, identified data.

`children`

    

A key path to a property whose non-`nil` value gives the children of a data
element. A non-`nil` but empty value denotes an element capable of having
children that’s currently childless, such as an empty directory in a file
system. On the other hand, if the property at the key path is `nil`, then the
outline group treats the data element as a leaf in the tree, like a regular
file in a file system.

`content`

    

A view builder that produces a content view based on a data element.

## Discussion

This initializer creates an instance that uniquely identifies views across
updates based on the identity of the underlying data element.

All generated disclosure groups begin in the collapsed state.

Make sure that the identifier of a data element only changes if you mean to
replace that element with a new element, one with a new identity. If the ID of
an element changes, then the content view generated from that element will
lose any current state and animations.

## See Also

### Creating an outline group

`init<DataElement>(Data, children: KeyPath<DataElement, Data?>, content:
(DataElement) -> Leaf)`

Creates an outline group from a collection of root data elements and a key
path to its children.

Available when `Data` conforms to `RandomAccessCollection`, `ID` is
`Data.Element.ID`, `Parent` conforms to `View`, `Parent` is `Leaf`, `Subgroup`
is `DisclosureGroup<Parent, OutlineSubgroupChildren>`, and `Data.Element`
conforms to `Identifiable`.

`init<DataElement>(DataElement, id: KeyPath<DataElement, ID>, children:
KeyPath<DataElement, Data?>, content: (DataElement) -> Leaf)`

Creates an outline group from a root data element, the key path to its
identifier, and a key path to its children.

Available when `Data` conforms to `RandomAccessCollection`, `ID` conforms to
`Hashable`, `Parent` conforms to `View`, `Parent` is `Leaf`, and `Subgroup` is
`DisclosureGroup<Parent, OutlineSubgroupChildren>`.

`init<DataElement>(Data, id: KeyPath<DataElement, ID>, children:
KeyPath<DataElement, Data?>, content: (DataElement) -> Leaf)`

Creates an outline group from a collection of root data elements, the key path
to a data element’s identifier, and a key path to its children.

Available when `Data` conforms to `RandomAccessCollection`, `ID` conforms to
`Hashable`, `Parent` conforms to `View`, `Parent` is `Leaf`, and `Subgroup` is
`DisclosureGroup<Parent, OutlineSubgroupChildren>`.

Initializer

# init(_:children:content:)

Creates an outline group from a collection of root data elements and a key
path to its children.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    init<DataElement>(
        _ data: Data,
        children: KeyPath<DataElement, Data?>,
        @ViewBuilder content: @escaping (DataElement) -> Leaf
    ) where ID == DataElement.ID, DataElement : Identifiable, DataElement == Data.Element

Available when `Data` conforms to `RandomAccessCollection`, `ID` is
`Data.Element.ID`, `Parent` conforms to `View`, `Parent` is `Leaf`, `Subgroup`
is `DisclosureGroup<Parent, OutlineSubgroupChildren>`, and `Data.Element`
conforms to `Identifiable`.

##  Parameters

`data`

    

A collection of tree-structured, identified data.

`children`

    

A key path to a property whose non-`nil` value gives the children of `data`. A
non-`nil` but empty value denotes an element capable of having children that’s
currently childless, such as an empty directory in a file system. On the other
hand, if the property at the key path is `nil`, then the outline group treats
`data` as a leaf in the tree, like a regular file in a file system.

`content`

    

A view builder that produces a content view based on an element in `data`.

## Discussion

This initializer creates an instance that uniquely identifies views across
updates based on the identity of the underlying data element.

All generated disclosure groups begin in the collapsed state.

Make sure that the identifier of a data element only changes if you mean to
replace that element with a new element, one with a new identity. If the ID of
an element changes, then the content view generated from that element will
lose any current state and animations.

## See Also

### Creating an outline group

`init<DataElement>(DataElement, children: KeyPath<DataElement, Data?>,
content: (DataElement) -> Leaf)`

Creates an outline group from a root data element and a key path to its
children.

Available when `Data` conforms to `RandomAccessCollection`, `ID` is
`Data.Element.ID`, `Parent` conforms to `View`, `Parent` is `Leaf`, `Subgroup`
is `DisclosureGroup<Parent, OutlineSubgroupChildren>`, and `Data.Element`
conforms to `Identifiable`.

`init<DataElement>(DataElement, id: KeyPath<DataElement, ID>, children:
KeyPath<DataElement, Data?>, content: (DataElement) -> Leaf)`

Creates an outline group from a root data element, the key path to its
identifier, and a key path to its children.

Available when `Data` conforms to `RandomAccessCollection`, `ID` conforms to
`Hashable`, `Parent` conforms to `View`, `Parent` is `Leaf`, and `Subgroup` is
`DisclosureGroup<Parent, OutlineSubgroupChildren>`.

`init<DataElement>(Data, id: KeyPath<DataElement, ID>, children:
KeyPath<DataElement, Data?>, content: (DataElement) -> Leaf)`

Creates an outline group from a collection of root data elements, the key path
to a data element’s identifier, and a key path to its children.

Available when `Data` conforms to `RandomAccessCollection`, `ID` conforms to
`Hashable`, `Parent` conforms to `View`, `Parent` is `Leaf`, and `Subgroup` is
`DisclosureGroup<Parent, OutlineSubgroupChildren>`.

Initializer

# init(_:id:children:content:)

Creates an outline group from a root data element, the key path to its
identifier, and a key path to its children.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    init<DataElement>(
        _ root: DataElement,
        id: KeyPath<DataElement, ID>,
        children: KeyPath<DataElement, Data?>,
        @ViewBuilder content: @escaping (DataElement) -> Leaf
    ) where DataElement == Data.Element

Available when `Data` conforms to `RandomAccessCollection`, `ID` conforms to
`Hashable`, `Parent` conforms to `View`, `Parent` is `Leaf`, and `Subgroup` is
`DisclosureGroup<Parent, OutlineSubgroupChildren>`.

##  Parameters

`root`

    

The root of a collection of tree-structured, identified data.

`id`

    

The key path to a data element’s identifier.

`children`

    

A key path to a property whose non-`nil` value gives the children of a data
element. A non-`nil` but empty value denotes an element capable of having
children that’s currently childless, such as an empty directory in a file
system. On the other hand, if the property at the key path is `nil`, then the
outline group treats the data element as a leaf in the tree, like a regular
file in a file system.

`content`

    

A view builder that produces a content view based on a data element.

## Discussion

This initializer creates an instance that uniquely identifies views across
updates based on the identity of the underlying data element.

All generated disclosure groups begin in the collapsed state.

Make sure that the identifier of a data element only changes if you mean to
replace that element with a new element, one with a new identity. If the ID of
an element changes, then the content view generated from that element will
lose any current state and animations.

## See Also

### Creating an outline group

`init<DataElement>(DataElement, children: KeyPath<DataElement, Data?>,
content: (DataElement) -> Leaf)`

Creates an outline group from a root data element and a key path to its
children.

Available when `Data` conforms to `RandomAccessCollection`, `ID` is
`Data.Element.ID`, `Parent` conforms to `View`, `Parent` is `Leaf`, `Subgroup`
is `DisclosureGroup<Parent, OutlineSubgroupChildren>`, and `Data.Element`
conforms to `Identifiable`.

`init<DataElement>(Data, children: KeyPath<DataElement, Data?>, content:
(DataElement) -> Leaf)`

Creates an outline group from a collection of root data elements and a key
path to its children.

Available when `Data` conforms to `RandomAccessCollection`, `ID` is
`Data.Element.ID`, `Parent` conforms to `View`, `Parent` is `Leaf`, `Subgroup`
is `DisclosureGroup<Parent, OutlineSubgroupChildren>`, and `Data.Element`
conforms to `Identifiable`.

`init<DataElement>(Data, id: KeyPath<DataElement, ID>, children:
KeyPath<DataElement, Data?>, content: (DataElement) -> Leaf)`

Creates an outline group from a collection of root data elements, the key path
to a data element’s identifier, and a key path to its children.

Available when `Data` conforms to `RandomAccessCollection`, `ID` conforms to
`Hashable`, `Parent` conforms to `View`, `Parent` is `Leaf`, and `Subgroup` is
`DisclosureGroup<Parent, OutlineSubgroupChildren>`.

Initializer

# init(_:id:children:content:)

Creates an outline group from a collection of root data elements, the key path
to a data element’s identifier, and a key path to its children.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    init<DataElement>(
        _ data: Data,
        id: KeyPath<DataElement, ID>,
        children: KeyPath<DataElement, Data?>,
        @ViewBuilder content: @escaping (DataElement) -> Leaf
    ) where DataElement == Data.Element

Available when `Data` conforms to `RandomAccessCollection`, `ID` conforms to
`Hashable`, `Parent` conforms to `View`, `Parent` is `Leaf`, and `Subgroup` is
`DisclosureGroup<Parent, OutlineSubgroupChildren>`.

##  Parameters

`data`

    

A collection of tree-structured, identified data.

`id`

    

The key path to a data element’s identifier.

`children`

    

A key path to a property whose non-`nil` value gives the children of `data`. A
non-`nil` but empty value denotes an element capable of having children that’s
currently childless, such as an empty directory in a file system. On the other
hand, if the property at the key path is `nil`, then the outline group treats
`data` as a leaf in the tree, like a regular file in a file system.

`content`

    

A view builder that produces a content view based on an element in `data`.

## Discussion

This initializer creates an instance that uniquely identifies views across
updates based on the identity of the underlying data element.

All generated disclosure groups begin in the collapsed state.

Make sure that the identifier of a data element only changes if you mean to
replace that element with a new element, one with a new identity. If the ID of
an element changes, then the content view generated from that element will
lose any current state and animations.

## See Also

### Creating an outline group

`init<DataElement>(DataElement, children: KeyPath<DataElement, Data?>,
content: (DataElement) -> Leaf)`

Creates an outline group from a root data element and a key path to its
children.

Available when `Data` conforms to `RandomAccessCollection`, `ID` is
`Data.Element.ID`, `Parent` conforms to `View`, `Parent` is `Leaf`, `Subgroup`
is `DisclosureGroup<Parent, OutlineSubgroupChildren>`, and `Data.Element`
conforms to `Identifiable`.

`init<DataElement>(Data, children: KeyPath<DataElement, Data?>, content:
(DataElement) -> Leaf)`

Creates an outline group from a collection of root data elements and a key
path to its children.

Available when `Data` conforms to `RandomAccessCollection`, `ID` is
`Data.Element.ID`, `Parent` conforms to `View`, `Parent` is `Leaf`, `Subgroup`
is `DisclosureGroup<Parent, OutlineSubgroupChildren>`, and `Data.Element`
conforms to `Identifiable`.

`init<DataElement>(DataElement, id: KeyPath<DataElement, ID>, children:
KeyPath<DataElement, Data?>, content: (DataElement) -> Leaf)`

Creates an outline group from a root data element, the key path to its
identifier, and a key path to its children.

Available when `Data` conforms to `RandomAccessCollection`, `ID` conforms to
`Hashable`, `Parent` conforms to `View`, `Parent` is `Leaf`, and `Subgroup` is
`DisclosureGroup<Parent, OutlineSubgroupChildren>`.

Initializer

# init(_:children:content:)

Creates an outline group from a binding to a root data element and a key path
to its children.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  visionOS 1.0+

    
    
    init<C, E>(
        _ root: Binding<E>,
        children: WritableKeyPath<E, C?>,
        @ViewBuilder content: @escaping (Binding<E>) -> Leaf
    ) where Data == Binding<C>, ID == E.ID, C : MutableCollection, C : RandomAccessCollection, E : Identifiable, E == C.Element

Available when `Data` conforms to `RandomAccessCollection`, `ID` is
`Data.Element.ID`, `Parent` conforms to `View`, `Parent` is `Leaf`, `Subgroup`
is `DisclosureGroup<Parent, OutlineSubgroupChildren>`, and `Data.Element`
conforms to `Identifiable`.

##  Parameters

`root`

    

The root of a collection of tree-structured, identified data.

`children`

    

A key path to a property whose non-`nil` value gives the children of a data
element. A non-`nil` but empty value denotes an element capable of having
children that’s currently childless, such as an empty directory in a file
system. On the other hand, if the property at the key path is `nil`, then the
outline group treats the data element as a leaf in the tree, like a regular
file in a file system.

`content`

    

A view builder that produces a content view based on a data element.

## Discussion

This initializer creates an instance that uniquely identifies views across
updates based on the identity of the underlying data element.

All generated disclosure groups begin in the collapsed state.

Make sure that the identifier of a data element only changes if you mean to
replace that element with a new element, one with a new identity. If the ID of
an element changes, then the content view generated from that element will
lose any current state and animations.

## See Also

### Creating an outline group from a binding

`init<C, E>(Binding<C>, children: WritableKeyPath<E, C?>, content:
(Binding<E>) -> Leaf)`

Creates an outline group from a binding to a collection of root data elements
and a key path to its children.

Available when `Data` conforms to `RandomAccessCollection`, `ID` is
`Data.Element.ID`, `Parent` conforms to `View`, `Parent` is `Leaf`, `Subgroup`
is `DisclosureGroup<Parent, OutlineSubgroupChildren>`, and `Data.Element`
conforms to `Identifiable`.

`init<C, E>(Binding<E>, id: KeyPath<E, ID>, children: WritableKeyPath<E, C?>,
content: (Binding<E>) -> Leaf)`

Creates an outline group from a binding to a root data element, the key path
to its identifier, and a key path to its children.

Available when `Data` conforms to `RandomAccessCollection`, `ID` conforms to
`Hashable`, `Parent` conforms to `View`, `Parent` is `Leaf`, and `Subgroup` is
`DisclosureGroup<Parent, OutlineSubgroupChildren>`.

`init<C, E>(Binding<C>, id: KeyPath<E, ID>, children: WritableKeyPath<E, C?>,
content: (Binding<E>) -> Leaf)`

Creates an outline group from a binding to a collection of root data elements,
the key path to a data element’s identifier, and a key path to its children.

Available when `Data` conforms to `RandomAccessCollection`, `ID` conforms to
`Hashable`, `Parent` conforms to `View`, `Parent` is `Leaf`, and `Subgroup` is
`DisclosureGroup<Parent, OutlineSubgroupChildren>`.

Initializer

# init(_:children:content:)

Creates an outline group from a binding to a collection of root data elements
and a key path to its children.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  visionOS 1.0+

    
    
    init<C, E>(
        _ data: Binding<C>,
        children: WritableKeyPath<E, C?>,
        @ViewBuilder content: @escaping (Binding<E>) -> Leaf
    ) where Data == Binding<C>, ID == E.ID, C : MutableCollection, C : RandomAccessCollection, E : Identifiable, E == C.Element

Available when `Data` conforms to `RandomAccessCollection`, `ID` is
`Data.Element.ID`, `Parent` conforms to `View`, `Parent` is `Leaf`, `Subgroup`
is `DisclosureGroup<Parent, OutlineSubgroupChildren>`, and `Data.Element`
conforms to `Identifiable`.

##  Parameters

`data`

    

A collection of tree-structured, identified data.

`children`

    

A key path to a property whose non-`nil` value gives the children of `data`. A
non-`nil` but empty value denotes an element capable of having children that’s
currently childless, such as an empty directory in a file system. On the other
hand, if the property at the key path is `nil`, then the outline group treats
`data` as a leaf in the tree, like a regular file in a file system.

`content`

    

A view builder that produces a content view based on an element in `data`.

## Discussion

This initializer creates an instance that uniquely identifies views across
updates based on the identity of the underlying data element.

All generated disclosure groups begin in the collapsed state.

Make sure that the identifier of a data element only changes if you mean to
replace that element with a new element, one with a new identity. If the ID of
an element changes, then the content view generated from that element will
lose any current state and animations.

## See Also

### Creating an outline group from a binding

`init<C, E>(Binding<E>, children: WritableKeyPath<E, C?>, content:
(Binding<E>) -> Leaf)`

Creates an outline group from a binding to a root data element and a key path
to its children.

Available when `Data` conforms to `RandomAccessCollection`, `ID` is
`Data.Element.ID`, `Parent` conforms to `View`, `Parent` is `Leaf`, `Subgroup`
is `DisclosureGroup<Parent, OutlineSubgroupChildren>`, and `Data.Element`
conforms to `Identifiable`.

`init<C, E>(Binding<E>, id: KeyPath<E, ID>, children: WritableKeyPath<E, C?>,
content: (Binding<E>) -> Leaf)`

Creates an outline group from a binding to a root data element, the key path
to its identifier, and a key path to its children.

Available when `Data` conforms to `RandomAccessCollection`, `ID` conforms to
`Hashable`, `Parent` conforms to `View`, `Parent` is `Leaf`, and `Subgroup` is
`DisclosureGroup<Parent, OutlineSubgroupChildren>`.

`init<C, E>(Binding<C>, id: KeyPath<E, ID>, children: WritableKeyPath<E, C?>,
content: (Binding<E>) -> Leaf)`

Creates an outline group from a binding to a collection of root data elements,
the key path to a data element’s identifier, and a key path to its children.

Available when `Data` conforms to `RandomAccessCollection`, `ID` conforms to
`Hashable`, `Parent` conforms to `View`, `Parent` is `Leaf`, and `Subgroup` is
`DisclosureGroup<Parent, OutlineSubgroupChildren>`.

Initializer

# init(_:id:children:content:)

Creates an outline group from a binding to a root data element, the key path
to its identifier, and a key path to its children.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  visionOS 1.0+

    
    
    init<C, E>(
        _ root: Binding<E>,
        id: KeyPath<E, ID>,
        children: WritableKeyPath<E, C?>,
        @ViewBuilder content: @escaping (Binding<E>) -> Leaf
    ) where Data == Binding<C>, C : MutableCollection, C : RandomAccessCollection, E == C.Element

Available when `Data` conforms to `RandomAccessCollection`, `ID` conforms to
`Hashable`, `Parent` conforms to `View`, `Parent` is `Leaf`, and `Subgroup` is
`DisclosureGroup<Parent, OutlineSubgroupChildren>`.

##  Parameters

`root`

    

The root of a collection of tree-structured, identified data.

`id`

    

The key path to a data element’s identifier.

`children`

    

A key path to a property whose non-`nil` value gives the children of a data
element. A non-`nil` but empty value denotes an element capable of having
children that’s currently childless, such as an empty directory in a file
system. On the other hand, if the property at the key path is `nil`, then the
outline group treats the data element as a leaf in the tree, like a regular
file in a file system.

`content`

    

A view builder that produces a content view based on a data element.

## Discussion

This initializer creates an instance that uniquely identifies views across
updates based on the identity of the underlying data element.

All generated disclosure groups begin in the collapsed state.

Make sure that the identifier of a data element only changes if you mean to
replace that element with a new element, one with a new identity. If the ID of
an element changes, then the content view generated from that element will
lose any current state and animations.

## See Also

### Creating an outline group from a binding

`init<C, E>(Binding<E>, children: WritableKeyPath<E, C?>, content:
(Binding<E>) -> Leaf)`

Creates an outline group from a binding to a root data element and a key path
to its children.

Available when `Data` conforms to `RandomAccessCollection`, `ID` is
`Data.Element.ID`, `Parent` conforms to `View`, `Parent` is `Leaf`, `Subgroup`
is `DisclosureGroup<Parent, OutlineSubgroupChildren>`, and `Data.Element`
conforms to `Identifiable`.

`init<C, E>(Binding<C>, children: WritableKeyPath<E, C?>, content:
(Binding<E>) -> Leaf)`

Creates an outline group from a binding to a collection of root data elements
and a key path to its children.

Available when `Data` conforms to `RandomAccessCollection`, `ID` is
`Data.Element.ID`, `Parent` conforms to `View`, `Parent` is `Leaf`, `Subgroup`
is `DisclosureGroup<Parent, OutlineSubgroupChildren>`, and `Data.Element`
conforms to `Identifiable`.

`init<C, E>(Binding<C>, id: KeyPath<E, ID>, children: WritableKeyPath<E, C?>,
content: (Binding<E>) -> Leaf)`

Creates an outline group from a binding to a collection of root data elements,
the key path to a data element’s identifier, and a key path to its children.

Available when `Data` conforms to `RandomAccessCollection`, `ID` conforms to
`Hashable`, `Parent` conforms to `View`, `Parent` is `Leaf`, and `Subgroup` is
`DisclosureGroup<Parent, OutlineSubgroupChildren>`.

Initializer

# init(_:id:children:content:)

Creates an outline group from a binding to a collection of root data elements,
the key path to a data element’s identifier, and a key path to its children.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  visionOS 1.0+

    
    
    init<C, E>(
        _ data: Binding<C>,
        id: KeyPath<E, ID>,
        children: WritableKeyPath<E, C?>,
        @ViewBuilder content: @escaping (Binding<E>) -> Leaf
    ) where Data == Binding<C>, C : MutableCollection, C : RandomAccessCollection, E == C.Element

Available when `Data` conforms to `RandomAccessCollection`, `ID` conforms to
`Hashable`, `Parent` conforms to `View`, `Parent` is `Leaf`, and `Subgroup` is
`DisclosureGroup<Parent, OutlineSubgroupChildren>`.

##  Parameters

`data`

    

A collection of tree-structured, identified data.

`id`

    

The key path to a data element’s identifier.

`children`

    

A key path to a property whose non-`nil` value gives the children of `data`. A
non-`nil` but empty value denotes an element capable of having children that’s
currently childless, such as an empty directory in a file system. On the other
hand, if the property at the key path is `nil`, then the outline group treats
`data` as a leaf in the tree, like a regular file in a file system.

`content`

    

A view builder that produces a content view based on an element in `data`.

## Discussion

This initializer creates an instance that uniquely identifies views across
updates based on the identity of the underlying data element.

All generated disclosure groups begin in the collapsed state.

Make sure that the identifier of a data element only changes if you mean to
replace that element with a new element, one with a new identity. If the ID of
an element changes, then the content view generated from that element will
lose any current state and animations.

## See Also

### Creating an outline group from a binding

`init<C, E>(Binding<E>, children: WritableKeyPath<E, C?>, content:
(Binding<E>) -> Leaf)`

Creates an outline group from a binding to a root data element and a key path
to its children.

Available when `Data` conforms to `RandomAccessCollection`, `ID` is
`Data.Element.ID`, `Parent` conforms to `View`, `Parent` is `Leaf`, `Subgroup`
is `DisclosureGroup<Parent, OutlineSubgroupChildren>`, and `Data.Element`
conforms to `Identifiable`.

`init<C, E>(Binding<C>, children: WritableKeyPath<E, C?>, content:
(Binding<E>) -> Leaf)`

Creates an outline group from a binding to a collection of root data elements
and a key path to its children.

Available when `Data` conforms to `RandomAccessCollection`, `ID` is
`Data.Element.ID`, `Parent` conforms to `View`, `Parent` is `Leaf`, `Subgroup`
is `DisclosureGroup<Parent, OutlineSubgroupChildren>`, and `Data.Element`
conforms to `Identifiable`.

`init<C, E>(Binding<E>, id: KeyPath<E, ID>, children: WritableKeyPath<E, C?>,
content: (Binding<E>) -> Leaf)`

Creates an outline group from a binding to a root data element, the key path
to its identifier, and a key path to its children.

Available when `Data` conforms to `RandomAccessCollection`, `ID` conforms to
`Hashable`, `Parent` conforms to `View`, `Parent` is `Leaf`, and `Subgroup` is
`DisclosureGroup<Parent, OutlineSubgroupChildren>`.

Initializer

# init(_:children:)

Creates an outline group from a root data element and a key path to its
children.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    init<DataElement>(
        _ root: DataElement,
        children: KeyPath<DataElement, Data?>
    ) where ID == DataElement.ID, Parent == TableRow<DataElement>, Leaf == TableRow<DataElement>, Subgroup == TableRow<DataElement>, DataElement : Identifiable, DataElement == Data.Element

Available when `Data` conforms to `RandomAccessCollection`, `ID` is
`Data.Element.ID`, `Parent` conforms to `TableRowContent`, `Parent` is `Leaf`,
`Leaf` is `Subgroup`, and `Data.Element` is `Parent.TableRowValue`.

##  Parameters

`root`

    

The root of a collection of tree-structured, identified data.

`children`

    

A key path to a property whose non-`nil` value gives the children of `data`. A
non-`nil` but empty value denotes an element capable of having children that’s
currently childless, such as an empty directory in a file system. On the other
hand, if the property at the key path is `nil`, then the outline group treats
`data` as a leaf in the tree, like a regular file in a file system.

## Discussion

This initializer provides a default `TableRowBuilder` using `TableRow` for
each data element.

This initializer creates an instance that uniquely identifies table rows
across updates based on the identity of the underlying data element.

All generated disclosure groups begin in the collapsed state.

## See Also

### Creating an outline group in a table

`init<DataElement>(Data, children: KeyPath<DataElement, Data?>)`

Creates an outline group from a collection of root data elements and a key
path to element’s children.

Available when `Data` conforms to `RandomAccessCollection`, `ID` is
`Data.Element.ID`, `Parent` conforms to `TableRowContent`, `Parent` is `Leaf`,
`Leaf` is `Subgroup`, and `Data.Element` is `Parent.TableRowValue`.

`init<DataElement>(Data, children: KeyPath<DataElement, Data?>, content:
(DataElement) -> Leaf)`

Creates an outline group from a collection of root data elements and a key
path to element’s children.

Available when `Data` conforms to `RandomAccessCollection`, `ID` is
`Data.Element.ID`, `Parent` conforms to `TableRowContent`, `Parent` is `Leaf`,
`Leaf` is `Subgroup`, and `Data.Element` is `Parent.TableRowValue`.

`init<DataElement>(DataElement, children: KeyPath<DataElement, Data?>,
content: (DataElement) -> Leaf)`

Creates an outline group from a root data element and a key path to its
children.

Available when `Data` conforms to `RandomAccessCollection`, `ID` is
`Data.Element.ID`, `Parent` conforms to `TableRowContent`, `Parent` is `Leaf`,
`Leaf` is `Subgroup`, and `Data.Element` is `Parent.TableRowValue`.

`init<DataElement>(DataElement, id: KeyPath<DataElement, ID>, children:
KeyPath<DataElement, Data?>, content: (DataElement) -> Leaf)`

Creates an outline group from a root data element, a key path to the its
identifier, as well as a key path to its children.

Available when `Data` conforms to `RandomAccessCollection`, `ID` is
`Data.Element.ID`, `Parent` conforms to `TableRowContent`, `Parent` is `Leaf`,
`Leaf` is `Subgroup`, and `Data.Element` is `Parent.TableRowValue`.

`init<DataElement>(DataElement, id: KeyPath<DataElement, ID>, children:
KeyPath<DataElement, Data?>, content: (DataElement) -> Leaf)`

Creates an outline group from a root data element, a key path to the its
identifier, as well as a key path to its children.

Available when `Data` conforms to `RandomAccessCollection`, `ID` is
`Data.Element.ID`, `Parent` conforms to `TableRowContent`, `Parent` is `Leaf`,
`Leaf` is `Subgroup`, and `Data.Element` is `Parent.TableRowValue`.

Initializer

# init(_:children:)

Creates an outline group from a collection of root data elements and a key
path to element’s children.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    init<DataElement>(
        _ data: Data,
        children: KeyPath<DataElement, Data?>
    ) where ID == DataElement.ID, Parent == TableRow<DataElement>, Leaf == TableRow<DataElement>, Subgroup == TableRow<DataElement>, DataElement : Identifiable, DataElement == Data.Element

Available when `Data` conforms to `RandomAccessCollection`, `ID` is
`Data.Element.ID`, `Parent` conforms to `TableRowContent`, `Parent` is `Leaf`,
`Leaf` is `Subgroup`, and `Data.Element` is `Parent.TableRowValue`.

##  Parameters

`data`

    

A collection of tree-structured, identified data.

`children`

    

A key path to a property whose non-`nil` value gives the children of `data`. A
non-`nil` but empty value denotes an element capable of having children that’s
currently childless, such as an empty directory in a file system. On the other
hand, if the property at the key path is `nil`, then the outline group treats
`data` as a leaf in the tree, like a regular file in a file system.

## Discussion

This initializer provides a default `TableRowBuilder` using `TableRow` for
each data element.

This initializer creates an instance that uniquely identifies table rows
across updates based on the identity of the underlying data element.

All generated disclosure groups begin in the collapsed state.

## See Also

### Creating an outline group in a table

`init<DataElement>(DataElement, children: KeyPath<DataElement, Data?>)`

Creates an outline group from a root data element and a key path to its
children.

Available when `Data` conforms to `RandomAccessCollection`, `ID` is
`Data.Element.ID`, `Parent` conforms to `TableRowContent`, `Parent` is `Leaf`,
`Leaf` is `Subgroup`, and `Data.Element` is `Parent.TableRowValue`.

`init<DataElement>(Data, children: KeyPath<DataElement, Data?>, content:
(DataElement) -> Leaf)`

Creates an outline group from a collection of root data elements and a key
path to element’s children.

Available when `Data` conforms to `RandomAccessCollection`, `ID` is
`Data.Element.ID`, `Parent` conforms to `TableRowContent`, `Parent` is `Leaf`,
`Leaf` is `Subgroup`, and `Data.Element` is `Parent.TableRowValue`.

`init<DataElement>(DataElement, children: KeyPath<DataElement, Data?>,
content: (DataElement) -> Leaf)`

Creates an outline group from a root data element and a key path to its
children.

Available when `Data` conforms to `RandomAccessCollection`, `ID` is
`Data.Element.ID`, `Parent` conforms to `TableRowContent`, `Parent` is `Leaf`,
`Leaf` is `Subgroup`, and `Data.Element` is `Parent.TableRowValue`.

`init<DataElement>(DataElement, id: KeyPath<DataElement, ID>, children:
KeyPath<DataElement, Data?>, content: (DataElement) -> Leaf)`

Creates an outline group from a root data element, a key path to the its
identifier, as well as a key path to its children.

Available when `Data` conforms to `RandomAccessCollection`, `ID` is
`Data.Element.ID`, `Parent` conforms to `TableRowContent`, `Parent` is `Leaf`,
`Leaf` is `Subgroup`, and `Data.Element` is `Parent.TableRowValue`.

`init<DataElement>(DataElement, id: KeyPath<DataElement, ID>, children:
KeyPath<DataElement, Data?>, content: (DataElement) -> Leaf)`

Creates an outline group from a root data element, a key path to the its
identifier, as well as a key path to its children.

Available when `Data` conforms to `RandomAccessCollection`, `ID` is
`Data.Element.ID`, `Parent` conforms to `TableRowContent`, `Parent` is `Leaf`,
`Leaf` is `Subgroup`, and `Data.Element` is `Parent.TableRowValue`.

Initializer

# init(_:children:content:)

Creates an outline group from a collection of root data elements and a key
path to element’s children.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    init<DataElement>(
        _ data: Data,
        children: KeyPath<DataElement, Data?>,
        @TableRowBuilder<DataElement> content: @escaping (DataElement) -> Leaf
    ) where ID == DataElement.ID, DataElement == Data.Element

Available when `Data` conforms to `RandomAccessCollection`, `ID` is
`Data.Element.ID`, `Parent` conforms to `TableRowContent`, `Parent` is `Leaf`,
`Leaf` is `Subgroup`, and `Data.Element` is `Parent.TableRowValue`.

##  Parameters

`data`

    

A collection of tree-structured, identified data.

`children`

    

A key path to a property whose non-`nil` value gives the children of `data`. A
non-`nil` but empty value denotes an element capable of having children that’s
currently childless, such as an empty directory in a file system. On the other
hand, if the property at the key path is `nil`, then the outline group treats
`data` as a leaf in the tree, like a regular file in a file system.

`content`

    

A table row builder that produces a row based on an element in `data`.

## Discussion

This initializer exposes `content` as a `TableRowBuilder` to allow custom
table row content for each data element.

This initializer creates an instance that uniquely identifies table rows
across updates based on the identity of the underlying data element.

All generated disclosure groups begin in the collapsed state.

## See Also

### Creating an outline group in a table

`init<DataElement>(DataElement, children: KeyPath<DataElement, Data?>)`

Creates an outline group from a root data element and a key path to its
children.

Available when `Data` conforms to `RandomAccessCollection`, `ID` is
`Data.Element.ID`, `Parent` conforms to `TableRowContent`, `Parent` is `Leaf`,
`Leaf` is `Subgroup`, and `Data.Element` is `Parent.TableRowValue`.

`init<DataElement>(Data, children: KeyPath<DataElement, Data?>)`

Creates an outline group from a collection of root data elements and a key
path to element’s children.

Available when `Data` conforms to `RandomAccessCollection`, `ID` is
`Data.Element.ID`, `Parent` conforms to `TableRowContent`, `Parent` is `Leaf`,
`Leaf` is `Subgroup`, and `Data.Element` is `Parent.TableRowValue`.

`init<DataElement>(DataElement, children: KeyPath<DataElement, Data?>,
content: (DataElement) -> Leaf)`

Creates an outline group from a root data element and a key path to its
children.

Available when `Data` conforms to `RandomAccessCollection`, `ID` is
`Data.Element.ID`, `Parent` conforms to `TableRowContent`, `Parent` is `Leaf`,
`Leaf` is `Subgroup`, and `Data.Element` is `Parent.TableRowValue`.

`init<DataElement>(DataElement, id: KeyPath<DataElement, ID>, children:
KeyPath<DataElement, Data?>, content: (DataElement) -> Leaf)`

Creates an outline group from a root data element, a key path to the its
identifier, as well as a key path to its children.

Available when `Data` conforms to `RandomAccessCollection`, `ID` is
`Data.Element.ID`, `Parent` conforms to `TableRowContent`, `Parent` is `Leaf`,
`Leaf` is `Subgroup`, and `Data.Element` is `Parent.TableRowValue`.

`init<DataElement>(DataElement, id: KeyPath<DataElement, ID>, children:
KeyPath<DataElement, Data?>, content: (DataElement) -> Leaf)`

Creates an outline group from a root data element, a key path to the its
identifier, as well as a key path to its children.

Available when `Data` conforms to `RandomAccessCollection`, `ID` is
`Data.Element.ID`, `Parent` conforms to `TableRowContent`, `Parent` is `Leaf`,
`Leaf` is `Subgroup`, and `Data.Element` is `Parent.TableRowValue`.

Initializer

# init(_:children:content:)

Creates an outline group from a root data element and a key path to its
children.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    init<DataElement>(
        _ root: DataElement,
        children: KeyPath<DataElement, Data?>,
        @TableRowBuilder<DataElement> content: @escaping (DataElement) -> Leaf
    ) where ID == DataElement.ID, DataElement == Data.Element

Available when `Data` conforms to `RandomAccessCollection`, `ID` is
`Data.Element.ID`, `Parent` conforms to `TableRowContent`, `Parent` is `Leaf`,
`Leaf` is `Subgroup`, and `Data.Element` is `Parent.TableRowValue`.

##  Parameters

`root`

    

The root of a collection of tree-structured, identified data.

`children`

    

A key path to a property whose non-`nil` value gives the children of `data`. A
non-`nil` but empty value denotes an element capable of having children that’s
currently childless, such as an empty directory in a file system. On the other
hand, if the property at the key path is `nil`, then the outline group treats
`data` as a leaf in the tree, like a regular file in a file system.

`content`

    

A table row builder that produces a row based on an element in `data`.

## Discussion

This initializer exposes `content` as a `TableRowBuilder` to allow custom
table row content for each data element.

This initializer creates an instance that uniquely identifies table rows
across updates based on the identity of the underlying data element.

All generated disclosure groups begin in the collapsed state.

## See Also

### Creating an outline group in a table

`init<DataElement>(DataElement, children: KeyPath<DataElement, Data?>)`

Creates an outline group from a root data element and a key path to its
children.

Available when `Data` conforms to `RandomAccessCollection`, `ID` is
`Data.Element.ID`, `Parent` conforms to `TableRowContent`, `Parent` is `Leaf`,
`Leaf` is `Subgroup`, and `Data.Element` is `Parent.TableRowValue`.

`init<DataElement>(Data, children: KeyPath<DataElement, Data?>)`

Creates an outline group from a collection of root data elements and a key
path to element’s children.

Available when `Data` conforms to `RandomAccessCollection`, `ID` is
`Data.Element.ID`, `Parent` conforms to `TableRowContent`, `Parent` is `Leaf`,
`Leaf` is `Subgroup`, and `Data.Element` is `Parent.TableRowValue`.

`init<DataElement>(Data, children: KeyPath<DataElement, Data?>, content:
(DataElement) -> Leaf)`

Creates an outline group from a collection of root data elements and a key
path to element’s children.

Available when `Data` conforms to `RandomAccessCollection`, `ID` is
`Data.Element.ID`, `Parent` conforms to `TableRowContent`, `Parent` is `Leaf`,
`Leaf` is `Subgroup`, and `Data.Element` is `Parent.TableRowValue`.

`init<DataElement>(DataElement, id: KeyPath<DataElement, ID>, children:
KeyPath<DataElement, Data?>, content: (DataElement) -> Leaf)`

Creates an outline group from a root data element, a key path to the its
identifier, as well as a key path to its children.

Available when `Data` conforms to `RandomAccessCollection`, `ID` is
`Data.Element.ID`, `Parent` conforms to `TableRowContent`, `Parent` is `Leaf`,
`Leaf` is `Subgroup`, and `Data.Element` is `Parent.TableRowValue`.

`init<DataElement>(DataElement, id: KeyPath<DataElement, ID>, children:
KeyPath<DataElement, Data?>, content: (DataElement) -> Leaf)`

Creates an outline group from a root data element, a key path to the its
identifier, as well as a key path to its children.

Available when `Data` conforms to `RandomAccessCollection`, `ID` is
`Data.Element.ID`, `Parent` conforms to `TableRowContent`, `Parent` is `Leaf`,
`Leaf` is `Subgroup`, and `Data.Element` is `Parent.TableRowValue`.

Initializer

# init(_:id:children:content:)

Creates an outline group from a root data element, a key path to the its
identifier, as well as a key path to its children.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    init<DataElement>(
        _ root: DataElement,
        id: KeyPath<DataElement, ID>,
        children: KeyPath<DataElement, Data?>,
        @TableRowBuilder<DataElement> content: @escaping (DataElement) -> Leaf
    ) where ID == DataElement.ID, DataElement == Data.Element

Available when `Data` conforms to `RandomAccessCollection`, `ID` is
`Data.Element.ID`, `Parent` conforms to `TableRowContent`, `Parent` is `Leaf`,
`Leaf` is `Subgroup`, and `Data.Element` is `Parent.TableRowValue`.

##  Parameters

`root`

    

The root of a collection of tree-structured, identified data.

`id`

    

The key path to a data element’s identifier.

`children`

    

A key path to a property whose non-`nil` value gives the children of `data`. A
non-`nil` but empty value denotes an element capable of having children that’s
currently childless, such as an empty directory in a file system. On the other
hand, if the property at the key path is `nil`, then the outline group treats
`data` as a leaf in the tree, like a regular file in a file system.

`content`

    

A view builder that produces a content view based on an element in `data`.

## Discussion

This initializer exposes `content` as a `TableRowBuilder` to allow custom
table row content for each data element.

This initializer creates an instance that uniquely identifies views across
updates based on the identity of the underlying data element.

All generated disclosure groups begin in the collapsed state.

Make sure that the identifier of a data element only changes if you mean to
replace that element with a new element, one with a new identity. If the ID of
an element changes, then the content view generated from that element will
lose any current state and animations.

## See Also

### Creating an outline group in a table

`init<DataElement>(DataElement, children: KeyPath<DataElement, Data?>)`

Creates an outline group from a root data element and a key path to its
children.

Available when `Data` conforms to `RandomAccessCollection`, `ID` is
`Data.Element.ID`, `Parent` conforms to `TableRowContent`, `Parent` is `Leaf`,
`Leaf` is `Subgroup`, and `Data.Element` is `Parent.TableRowValue`.

`init<DataElement>(Data, children: KeyPath<DataElement, Data?>)`

Creates an outline group from a collection of root data elements and a key
path to element’s children.

Available when `Data` conforms to `RandomAccessCollection`, `ID` is
`Data.Element.ID`, `Parent` conforms to `TableRowContent`, `Parent` is `Leaf`,
`Leaf` is `Subgroup`, and `Data.Element` is `Parent.TableRowValue`.

`init<DataElement>(Data, children: KeyPath<DataElement, Data?>, content:
(DataElement) -> Leaf)`

Creates an outline group from a collection of root data elements and a key
path to element’s children.

Available when `Data` conforms to `RandomAccessCollection`, `ID` is
`Data.Element.ID`, `Parent` conforms to `TableRowContent`, `Parent` is `Leaf`,
`Leaf` is `Subgroup`, and `Data.Element` is `Parent.TableRowValue`.

`init<DataElement>(DataElement, children: KeyPath<DataElement, Data?>,
content: (DataElement) -> Leaf)`

Creates an outline group from a root data element and a key path to its
children.

Available when `Data` conforms to `RandomAccessCollection`, `ID` is
`Data.Element.ID`, `Parent` conforms to `TableRowContent`, `Parent` is `Leaf`,
`Leaf` is `Subgroup`, and `Data.Element` is `Parent.TableRowValue`.

Initializer

# init(_:id:children:content:)

Creates an outline group from a root data element, a key path to the its
identifier, as well as a key path to its children.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    init<DataElement>(
        _ root: DataElement,
        id: KeyPath<DataElement, ID>,
        children: KeyPath<DataElement, Data?>,
        @TableRowBuilder<DataElement> content: @escaping (DataElement) -> Leaf
    ) where ID == DataElement.ID, DataElement == Data.Element

Available when `Data` conforms to `RandomAccessCollection`, `ID` is
`Data.Element.ID`, `Parent` conforms to `TableRowContent`, `Parent` is `Leaf`,
`Leaf` is `Subgroup`, and `Data.Element` is `Parent.TableRowValue`.

##  Parameters

`root`

    

The root of a collection of tree-structured, identified data.

`id`

    

The key path to a data element’s identifier.

`children`

    

A key path to a property whose non-`nil` value gives the children of `data`. A
non-`nil` but empty value denotes an element capable of having children that’s
currently childless, such as an empty directory in a file system. On the other
hand, if the property at the key path is `nil`, then the outline group treats
`data` as a leaf in the tree, like a regular file in a file system.

`content`

    

A view builder that produces a content view based on an element in `data`.

## Discussion

This initializer exposes `content` as a `TableRowBuilder` to allow custom
table row content for each data element.

This initializer creates an instance that uniquely identifies views across
updates based on the identity of the underlying data element.

All generated disclosure groups begin in the collapsed state.

Make sure that the identifier of a data element only changes if you mean to
replace that element with a new element, one with a new identity. If the ID of
an element changes, then the content view generated from that element will
lose any current state and animations.

## See Also

### Creating an outline group in a table

`init<DataElement>(DataElement, children: KeyPath<DataElement, Data?>)`

Creates an outline group from a root data element and a key path to its
children.

Available when `Data` conforms to `RandomAccessCollection`, `ID` is
`Data.Element.ID`, `Parent` conforms to `TableRowContent`, `Parent` is `Leaf`,
`Leaf` is `Subgroup`, and `Data.Element` is `Parent.TableRowValue`.

`init<DataElement>(Data, children: KeyPath<DataElement, Data?>)`

Creates an outline group from a collection of root data elements and a key
path to element’s children.

Available when `Data` conforms to `RandomAccessCollection`, `ID` is
`Data.Element.ID`, `Parent` conforms to `TableRowContent`, `Parent` is `Leaf`,
`Leaf` is `Subgroup`, and `Data.Element` is `Parent.TableRowValue`.

`init<DataElement>(Data, children: KeyPath<DataElement, Data?>, content:
(DataElement) -> Leaf)`

Creates an outline group from a collection of root data elements and a key
path to element’s children.

Available when `Data` conforms to `RandomAccessCollection`, `ID` is
`Data.Element.ID`, `Parent` conforms to `TableRowContent`, `Parent` is `Leaf`,
`Leaf` is `Subgroup`, and `Data.Element` is `Parent.TableRowValue`.

`init<DataElement>(DataElement, children: KeyPath<DataElement, Data?>,
content: (DataElement) -> Leaf)`

Creates an outline group from a root data element and a key path to its
children.

Available when `Data` conforms to `RandomAccessCollection`, `ID` is
`Data.Element.ID`, `Parent` conforms to `TableRowContent`, `Parent` is `Leaf`,
`Leaf` is `Subgroup`, and `Data.Element` is `Parent.TableRowValue`.

Structure

# OutlineSubgroupChildren

A type-erased view representing the children in an outline subgroup.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    struct OutlineSubgroupChildren

## Overview

`OutlineGroup` uses this type as a generic constraint for the `Content` of the
`DisclosureGroup` instances it creates.

## Relationships

### Conforms To

  * `View`

Initializer

# init(_:id:children:content:)

Creates an outline group from a collection of root data elements, a key path
to the element’s identifier, as well as a key path to element’s children.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    init<DataElement>(
        _ data: Data,
        id: KeyPath<DataElement, ID>,
        children: KeyPath<DataElement, Data?>,
        @TableRowBuilder<DataElement> content: @escaping (DataElement) -> Leaf
    ) where ID == DataElement.ID, DataElement == Data.Element

Available when `Data` conforms to `RandomAccessCollection`, `ID` is
`Data.Element.ID`, `Parent` conforms to `TableRowContent`, `Parent` is `Leaf`,
`Leaf` is `Subgroup`, and `Data.Element` is `Parent.TableRowValue`.

##  Parameters

`data`

    

A collection of tree-structured, identified data.

`id`

    

The key path to a data element’s identifier.

`children`

    

A key path to a property whose non-`nil` value gives the children of `data`. A
non-`nil` but empty value denotes an element capable of having children that’s
currently childless, such as an empty directory in a file system. On the other
hand, if the property at the key path is `nil`, then the outline group treats
`data` as a leaf in the tree, like a regular file in a file system.

`content`

    

A table row builder that produces a row based on an element in `data`.

## Discussion

This initializer exposes `content` as a `TableRowBuilder` to allow custom
table row content for each data element.

This initializer creates an instance that uniquely identifies table rows
across updates based on the identity of the underlying data element.

All generated disclosure groups begin in the collapsed state.



# OpenImmersiveSpaceAction

Instance Method

# callAsFunction(id:)

Presents an immersive space for the scene with the specified identifier.

visionOS 1.0+

    
    
    @discardableResult @MainActor
    func callAsFunction(id: String) async -> OpenImmersiveSpaceAction.Result

##  Parameters

`id`

    

The identifier of the immersive space to present.

## Discussion

Don’t call this method directly. SwiftUI calls it when you call the
`openImmersiveSpace` action with a string identifier:

For information about how Swift uses the `callAsFunction()` method to simplify
call site syntax, see Methods with Special Names in _The Swift Programming
Language_.

## See Also

### Calling the action

`func callAsFunction<D>(id: String, value: D) async ->
OpenImmersiveSpaceAction.Result`

Presents the immersive space that your app defines for the specified
identifier and that handles the type of the presented value.

`func callAsFunction<D>(value: D) async -> OpenImmersiveSpaceAction.Result`

Presents the immersive space that handles the type of the presented value.

Instance Method

# callAsFunction(id:value:)

Presents the immersive space that your app defines for the specified
identifier and that handles the type of the presented value.

visionOS 1.0+

    
    
    @discardableResult
    func callAsFunction<D>(
        id: String,
        value: D
    ) async -> OpenImmersiveSpaceAction.Result where D : Decodable, D : Encodable, D : Hashable

##  Parameters

`id`

    

The identifier of the immersive space to present.

`value`

    

The value to present.

## Discussion

Don’t call this method directly. SwiftUI calls it when you call the
`openImmersiveSpace` action with a string identifier and a value:

For information about how Swift uses the `callAsFunction()` method to simplify
call site syntax, see Methods with Special Names in _The Swift Programming
Language_.

## See Also

### Calling the action

`func callAsFunction(id: String) async -> OpenImmersiveSpaceAction.Result`

Presents an immersive space for the scene with the specified identifier.

`func callAsFunction<D>(value: D) async -> OpenImmersiveSpaceAction.Result`

Presents the immersive space that handles the type of the presented value.

Instance Method

# callAsFunction(value:)

Presents the immersive space that handles the type of the presented value.

visionOS 1.0+

    
    
    @discardableResult @MainActor
    func callAsFunction<D>(value: D) async -> OpenImmersiveSpaceAction.Result where D : Decodable, D : Encodable, D : Hashable

##  Parameters

`value`

    

The value to present.

## Discussion

Don’t call this method directly. SwiftUI calls it when you call the
`openImmersiveSpace` action with a value:

For information about how Swift uses the `callAsFunction()` method to simplify
call site syntax, see Methods with Special Names in _The Swift Programming
Language_.

## See Also

### Calling the action

`func callAsFunction(id: String) async -> OpenImmersiveSpaceAction.Result`

Presents an immersive space for the scene with the specified identifier.

`func callAsFunction<D>(id: String, value: D) async ->
OpenImmersiveSpaceAction.Result`

Presents the immersive space that your app defines for the specified
identifier and that handles the type of the presented value.

Enumeration

# OpenImmersiveSpaceAction.Result

The outcome of an attempt to open an immersive space.

visionOS 1.0+

    
    
    enum Result

## Topics

### Getting the result

`case opened`

The immersive space opened.

`case userCancelled`

The immersive space didn’t open because the user cancelled the operation.

`case error`

The system was unable to open the immersive space.

## Relationships

### Conforms To

  * `Equatable`
  * `Hashable`
  * `Sendable`



# OffsetTransition

Initializer

# init(_:)

Creates a transition that offset the view by the specified amount.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    init(_ offset: CGSize)

## See Also

### Creating the transition

`var offset: CGSize`

The amount to offset the view by.

Instance Property

# offset

The amount to offset the view by.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    var offset: CGSize

## See Also

### Creating the transition

`init(CGSize)`

Creates a transition that offset the view by the specified amount.



# OpenImmersiveSpaceAction.Result

Case

# OpenImmersiveSpaceAction.Result.opened

The immersive space opened.

visionOS 1.0+

    
    
    case opened

## See Also

### Getting the result

`case userCancelled`

The immersive space didn’t open because the user cancelled the operation.

`case error`

The system was unable to open the immersive space.

Case

# OpenImmersiveSpaceAction.Result.userCancelled

The immersive space didn’t open because the user cancelled the operation.

visionOS 1.0+

    
    
    case userCancelled

## See Also

### Getting the result

`case opened`

The immersive space opened.

`case error`

The system was unable to open the immersive space.

Case

# OpenImmersiveSpaceAction.Result.error

The system was unable to open the immersive space.

visionOS 1.0+

    
    
    case error

## See Also

### Getting the result

`case opened`

The immersive space opened.

`case userCancelled`

The immersive space didn’t open because the user cancelled the operation.



# OffsetShape

Initializer

# init(shape:offset:)

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init(
        shape: Content,
        offset: CGSize
    )

Instance Property

# offset

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var offset: CGSize

## See Also

### Getting the shape’s characteristics

`var shape: Content`

Instance Property

# shape

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var shape: Content

## See Also

### Getting the shape’s characteristics

`var offset: CGSize`

Instance Property

# animatableData

The data to animate.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var animatableData: OffsetShape<Content>.AnimatableData { get set }



# OpenURLAction

Initializer

# init(handler:)

Creates an action that opens a URL.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    init(handler: @escaping (URL) -> OpenURLAction.Result)

##  Parameters

`handler`

    

The closure to run for the given URL. The closure takes a URL as input, and
returns a `OpenURLAction.Result` that indicates the outcome of the action.

## Discussion

Use this initializer to create a custom action for opening URLs. Provide a
handler that takes a URL and returns an `OpenURLAction.Result`. Place your
handler in the environment using the `environment(_:_:)` view modifier:

Any views that read the action from the environment, including the built-in
`Link` view and `Text` views with markdown links, or links in attributed
strings, use your action.

SwiftUI translates the value that your custom action’s handler returns into an
appropriate Boolean result for the action call. For example, a view that uses
the action declared above receives `true` when calling the action, because the
handler always returns `handled`.

## See Also

### Creating the action

`struct Result`

The result of a custom open URL action.

Structure

# OpenURLAction.Result

The result of a custom open URL action.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    struct Result

## Overview

If you declare a custom `OpenURLAction` in the `Environment`, return one of
the result values from its handler.

  * Use `handled` to indicate that the handler opened the URL.

  * Use `discarded` to indicate that the handler discarded the URL.

  * Use `systemAction` without an argument to ask SwiftUI to open the URL with the system handler.

  * Use `systemAction(_:)` with a URL argument to ask SwiftUI to open the specified URL with the system handler.

You can use the last option to transform URLs, while still relying on the
system to open the URL. For example, you could append a path component to
every URL:

## Topics

### Getting the results

`static let discarded: OpenURLAction.Result`

The handler discarded the URL.

`static let handled: OpenURLAction.Result`

The handler opened the URL.

`static let systemAction: OpenURLAction.Result`

The handler asks the system to open the original URL.

`static func systemAction(URL) -> OpenURLAction.Result`

The handler asks the system to open the modified URL.

## See Also

### Creating the action

`init(handler: (URL) -> OpenURLAction.Result)`

Creates an action that opens a URL.

Instance Method

# callAsFunction(_:)

Opens a URL, following system conventions.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    func callAsFunction(_ url: URL)

##  Parameters

`url`

    

The URL to open.

## Discussion

Don’t call this method directly. SwiftUI calls it when you call the
`OpenURLAction` structure that you get from the `Environment`, using a URL as
an argument:

For information about how Swift uses the `callAsFunction()` method to simplify
call site syntax, see Methods with Special Names in _The Swift Programming
Language_.

## See Also

### Calling the action

`func callAsFunction(URL, completion: (Bool) -> Void)`

Asynchronously opens a URL, following system conventions.

Instance Method

# callAsFunction(_:completion:)

Asynchronously opens a URL, following system conventions.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  visionOS
1.0+

    
    
    func callAsFunction(
        _ url: URL,
        completion: @escaping (Bool) -> Void
    )

##  Parameters

`url`

    

The URL to open.

`completion`

    

A closure the method calls after determining if it can open the URL, but
possibly before fully opening the URL. The closure takes a Boolean value that
indicates whether the method can open the URL.

## Discussion

Don’t call this method directly. SwiftUI calls it when you call the
`OpenURLAction` structure that you get from the `Environment`, using a URL and
a completion handler as arguments:

For information about how Swift uses the `callAsFunction()` method to simplify
call site syntax, see Methods with Special Names in _The Swift Programming
Language_.

## See Also

### Calling the action

`func callAsFunction(URL)`

Opens a URL, following system conventions.



# OpenDocumentAction

Instance Method

# callAsFunction(at:)

Opens the document at the specified file URL.

macOS 13.0+

    
    
    func callAsFunction(at url: URL) async throws

##  Parameters

`url`

    

A file URL that points at an existing document.

## Discussion

Don’t call this method directly. SwiftUI calls it when you call the
`openDocument` action:

For information about how Swift uses the `callAsFunction()` method to simplify
call site syntax, see Methods with Special Names in _The Swift Programming
Language_.



# OrnamentAttachmentAnchor

Type Method

# scene(_:)

The anchor point for the ornament expressed as a unit point relative to the
scene.

visionOS 1.0+

    
    
    static func scene(_ anchor: UnitPoint) -> OrnamentAttachmentAnchor



# OpenWindowAction

Instance Method

# callAsFunction(id:)

Opens a window that’s associated with the specified identifier.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    func callAsFunction(id: String)

##  Parameters

`id`

    

The identifier of the scene to present.

## Discussion

Don’t call this method directly. SwiftUI calls it when you call the
`openWindow` action with an identifier:

For information about how Swift uses the `callAsFunction()` method to simplify
call site syntax, see Methods with Special Names in _The Swift Programming
Language_.

## See Also

### Calling the action

`func callAsFunction<D>(id: String, value: D)`

Opens a window defined by the window group that presents the specified value
type and that’s associated with the specified identifier.

`func callAsFunction<D>(value: D)`

Opens a window defined by a window group that presents the type of the
specified value.

Instance Method

# callAsFunction(id:value:)

Opens a window defined by the window group that presents the specified value
type and that’s associated with the specified identifier.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    func callAsFunction<D>(
        id: String,
        value: D
    ) where D : Decodable, D : Encodable, D : Hashable

##  Parameters

`id`

    

The identifier of the scene to present.

`value`

    

The value to present.

## Discussion

Don’t call this method directly. SwiftUI calls it when you call the
`openWindow` action with an identifier and a value:

For information about how Swift uses the `callAsFunction()` method to simplify
call site syntax, see Methods with Special Names in _The Swift Programming
Language_.

## See Also

### Calling the action

`func callAsFunction(id: String)`

Opens a window that’s associated with the specified identifier.

`func callAsFunction<D>(value: D)`

Opens a window defined by a window group that presents the type of the
specified value.

Instance Method

# callAsFunction(value:)

Opens a window defined by a window group that presents the type of the
specified value.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    func callAsFunction<D>(value: D) where D : Decodable, D : Encodable, D : Hashable

##  Parameters

`value`

    

The value to present.

## Discussion

Don’t call this method directly. SwiftUI calls it when you call the
`openWindow` action with a value:

For information about how Swift uses the `callAsFunction()` method to simplify
call site syntax, see Methods with Special Names in _The Swift Programming
Language_.

## See Also

### Calling the action

`func callAsFunction(id: String)`

Opens a window that’s associated with the specified identifier.

`func callAsFunction<D>(id: String, value: D)`

Opens a window defined by the window group that presents the specified value
type and that’s associated with the specified identifier.



