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

