Initializer

# init(selection:content:label:)

Creates a picker that displays a custom label.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init(
        selection: Binding<SelectionValue>,
        @ViewBuilder content: () -> Content,
        @ViewBuilder label: () -> Label
    )

Available when `Label` conforms to `View`, `SelectionValue` conforms to
`Hashable`, and `Content` conforms to `View`.

##  Parameters

`selection`

    

A binding to a property that determines the currently-selected option.

`content`

    

A view that contains the set of options.

`label`

    

A view that describes the purpose of selecting an option.

## See Also

### Creating a picker

`init(LocalizedStringKey, selection: Binding<SelectionValue>, content: () ->
Content)`

Creates a picker that generates its label from a localized string key.

Available when `Label` is `Text`, `SelectionValue` conforms to `Hashable`, and
`Content` conforms to `View`.

`init<S>(S, selection: Binding<SelectionValue>, content: () -> Content)`

Creates a picker that generates its label from a string.

Available when `Label` is `Text`, `SelectionValue` conforms to `Hashable`, and
`Content` conforms to `View`.

Initializer

# init(_:selection:content:)

Creates a picker that generates its label from a localized string key.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init(
        _ titleKey: LocalizedStringKey,
        selection: Binding<SelectionValue>,
        @ViewBuilder content: () -> Content
    )

Available when `Label` is `Text`, `SelectionValue` conforms to `Hashable`, and
`Content` conforms to `View`.

##  Parameters

`titleKey`

    

A localized string key that describes the purpose of selecting an option.

`selection`

    

A binding to a property that determines the currently-selected option.

`content`

    

A view that contains the set of options.

## Discussion

This initializer creates a `Text` view on your behalf, and treats the
localized key similar to `init(_:tableName:bundle:comment:)`. See `Text` for
more information about localizing strings.

To initialize a picker with a string variable, use
`init(_:selection:content:)` instead.

## See Also

### Creating a picker

`init(selection: Binding<SelectionValue>, content: () -> Content, label: () ->
Label)`

Creates a picker that displays a custom label.

Available when `Label` conforms to `View`, `SelectionValue` conforms to
`Hashable`, and `Content` conforms to `View`.

`init<S>(S, selection: Binding<SelectionValue>, content: () -> Content)`

Creates a picker that generates its label from a string.

Available when `Label` is `Text`, `SelectionValue` conforms to `Hashable`, and
`Content` conforms to `View`.

Initializer

# init(_:selection:content:)

Creates a picker that generates its label from a string.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init<S>(
        _ title: S,
        selection: Binding<SelectionValue>,
        @ViewBuilder content: () -> Content
    ) where S : StringProtocol

Available when `Label` is `Text`, `SelectionValue` conforms to `Hashable`, and
`Content` conforms to `View`.

##  Parameters

`title`

    

A string that describes the purpose of selecting an option.

`selection`

    

A binding to a property that determines the currently-selected option.

`content`

    

A view that contains the set of options.

## Discussion

This initializer creates a `Text` view on your behalf, and treats the title
similar to `init(_:)`. See `Text` for more information about localizing
strings.

To initialize a picker with a localized string key, use
`init(_:selection:content:)` instead.

## See Also

### Creating a picker

`init(selection: Binding<SelectionValue>, content: () -> Content, label: () ->
Label)`

Creates a picker that displays a custom label.

Available when `Label` conforms to `View`, `SelectionValue` conforms to
`Hashable`, and `Content` conforms to `View`.

`init(LocalizedStringKey, selection: Binding<SelectionValue>, content: () ->
Content)`

Creates a picker that generates its label from a localized string key.

Available when `Label` is `Text`, `SelectionValue` conforms to `Hashable`, and
`Content` conforms to `View`.

Initializer

# init(_:sources:selection:content:)

Creates a picker that generates its label from a localized string key.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    init<C>(
        _ titleKey: LocalizedStringKey,
        sources: C,
        selection: KeyPath<C.Element, Binding<SelectionValue>>,
        @ViewBuilder content: () -> Content
    ) where C : RandomAccessCollection

Available when `Label` is `Text`, `SelectionValue` conforms to `Hashable`, and
`Content` conforms to `View`.

##  Parameters

`titleKey`

    

A localized string key that describes the purpose of selecting an option.

`sources`

    

A collection of values used as the source for displaying the Picker’s
selection.

`selection`

    

The key path of the values that determines the currently-selected options.
When a user selects an option from the picker, the values at the key path of
all items in the `sources` collection are updated with the selected option.

`content`

    

A view that contains the set of options.

## Discussion

If the wrapped values of the collection passed to `sources` are not all the
same, some styles render the selection in a mixed state. The specific
presentation depends on the style. For example, a Picker with a menu style
uses dashes instead of checkmarks to indicate the selected values.

In the following example, a picker in a document inspector controls the
thickness of borders for the currently-selected shapes, which can be of any
number.

This initializer creates a `Text` view on your behalf, and treats the
localized key similar to `init(_:tableName:bundle:comment:)`. See `Text` for
more information about localizing strings.

## See Also

### Creating a picker for a collection

`init<C, S>(S, sources: C, selection: KeyPath<C.Element,
Binding<SelectionValue>>, content: () -> Content)`

Creates a picker bound to a collection of bindings that generates its label
from a string.

Available when `Label` is `Text`, `SelectionValue` conforms to `Hashable`, and
`Content` conforms to `View`.

`init<C>(sources: C, selection: KeyPath<C.Element, Binding<SelectionValue>>,
content: () -> Content, label: () -> Label)`

Creates a picker that displays a custom label.

Available when `Label` conforms to `View`, `SelectionValue` conforms to
`Hashable`, and `Content` conforms to `View`.

Initializer

# init(_:sources:selection:content:)

Creates a picker bound to a collection of bindings that generates its label
from a string.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    init<C, S>(
        _ title: S,
        sources: C,
        selection: KeyPath<C.Element, Binding<SelectionValue>>,
        @ViewBuilder content: () -> Content
    ) where C : RandomAccessCollection, S : StringProtocol

Available when `Label` is `Text`, `SelectionValue` conforms to `Hashable`, and
`Content` conforms to `View`.

##  Parameters

`title`

    

A string that describes the purpose of selecting an option.

`sources`

    

A collection of values used as the source for displaying the Picker’s
selection.

`selection`

    

The key path of the values that determines the currently-selected options.
When a user selects an option from the picker, the values at the key path of
all items in the `sources` collection are updated with the selected option.

`content`

    

A view that contains the set of options.

## Discussion

If the wrapped values of the collection passed to `sources` are not all the
same, some styles render the selection in a mixed state. The specific
presentation depends on the style. For example, a Picker with a menu style
uses dashes instead of checkmarks to indicate the selected values.

In the following example, a picker in a document inspector controls the
thickness of borders for the currently-selected shapes, which can be of any
number.

This initializer creates a `Text` view on your behalf, and treats the title
similar to `init(_:)`. See `Text` for more information about localizing
strings.

To initialize a picker with a localized string key, use
`init(_:sources:selection:content:)` instead.

## See Also

### Creating a picker for a collection

`init<C>(LocalizedStringKey, sources: C, selection: KeyPath<C.Element,
Binding<SelectionValue>>, content: () -> Content)`

Creates a picker that generates its label from a localized string key.

Available when `Label` is `Text`, `SelectionValue` conforms to `Hashable`, and
`Content` conforms to `View`.

`init<C>(sources: C, selection: KeyPath<C.Element, Binding<SelectionValue>>,
content: () -> Content, label: () -> Label)`

Creates a picker that displays a custom label.

Available when `Label` conforms to `View`, `SelectionValue` conforms to
`Hashable`, and `Content` conforms to `View`.

Initializer

# init(sources:selection:content:label:)

Creates a picker that displays a custom label.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    init<C>(
        sources: C,
        selection: KeyPath<C.Element, Binding<SelectionValue>>,
        @ViewBuilder content: () -> Content,
        @ViewBuilder label: () -> Label
    ) where C : RandomAccessCollection

Available when `Label` conforms to `View`, `SelectionValue` conforms to
`Hashable`, and `Content` conforms to `View`.

##  Parameters

`sources`

    

A collection of values used as the source for displaying the Picker’s
selection.

`selection`

    

The key path of the values that determines the currently-selected options.
When a user selects an option from the picker, the values at the key path of
all items in the `sources` collection are updated with the selected option.

`content`

    

A view that contains the set of options.

`label`

    

A view that describes the purpose of selecting an option.

## Discussion

If the wrapped values of the collection passed to `sources` are not all the
same, some styles render the selection in a mixed state. The specific
presentation depends on the style. For example, a Picker with a menu style
uses dashes instead of checkmarks to indicate the selected values.

In the following example, a picker in a document inspector controls the
thickness of borders for the currently-selected shapes, which can be of any
number.

## See Also

### Creating a picker for a collection

`init<C>(LocalizedStringKey, sources: C, selection: KeyPath<C.Element,
Binding<SelectionValue>>, content: () -> Content)`

Creates a picker that generates its label from a localized string key.

Available when `Label` is `Text`, `SelectionValue` conforms to `Hashable`, and
`Content` conforms to `View`.

`init<C, S>(S, sources: C, selection: KeyPath<C.Element,
Binding<SelectionValue>>, content: () -> Content)`

Creates a picker bound to a collection of bindings that generates its label
from a string.

Available when `Label` is `Text`, `SelectionValue` conforms to `Hashable`, and
`Content` conforms to `View`.

Initializer

# init(_:image:selection:content:)

Creates a picker that generates its label from a string and image resource.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    init<S>(
        _ title: S,
        image: ImageResource,
        selection: Binding<SelectionValue>,
        @ViewBuilder content: () -> Content
    ) where S : StringProtocol

Available when `Label` is `Label<Text, Image>`, `SelectionValue` conforms to
`Hashable`, and `Content` conforms to `View`.

##  Parameters

`title`

    

A string that describes the purpose of selecting an option.

`systemImage`

    

The name of the image resource to lookup.

`selection`

    

A binding to a property that determines the currently-selected option.

`content`

    

A view that contains the set of options.

## See Also

### Creating a picker with an image resource label

`init(LocalizedStringKey, image: ImageResource, selection:
Binding<SelectionValue>, content: () -> Content)`

Creates a picker that generates its label from a localized string key and
image resource

Available when `Label` is `Label<Text, Image>`, `SelectionValue` conforms to
`Hashable`, and `Content` conforms to `View`.

`init<C, S>(S, image: ImageResource, sources: C, selection: KeyPath<C.Element,
Binding<SelectionValue>>, content: () -> Content)`

Creates a picker bound to a collection of bindings that generates its label
from a string and image resource.

Available when `Label` is `Label<Text, Image>`, `SelectionValue` conforms to
`Hashable`, and `Content` conforms to `View`.

`init<C>(LocalizedStringKey, image: ImageResource, sources: C, selection:
KeyPath<C.Element, Binding<SelectionValue>>, content: () -> Content)`

Creates a picker that generates its label from a localized string key and
image resource.

Available when `Label` is `Label<Text, Image>`, `SelectionValue` conforms to
`Hashable`, and `Content` conforms to `View`.

Initializer

# init(_:image:selection:content:)

Creates a picker that generates its label from a localized string key and
image resource

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    init(
        _ titleKey: LocalizedStringKey,
        image: ImageResource,
        selection: Binding<SelectionValue>,
        @ViewBuilder content: () -> Content
    )

Available when `Label` is `Label<Text, Image>`, `SelectionValue` conforms to
`Hashable`, and `Content` conforms to `View`.

##  Parameters

`titleKey`

    

A localized string key that describes the purpose of selecting an option.

`image`

    

The name of the image resource to lookup.

`selection`

    

A binding to a property that determines the currently-selected option.

`content`

    

A view that contains the set of options.

## Discussion

This initializer creates a `Text` view on your behalf, and treats the
localized key similar to `init(_:tableName:bundle:comment:)`. See `Text` for
more information about localizing strings.

To initialize a picker with a string variable, use
`init(_:selection:content:)` instead.

## See Also

### Creating a picker with an image resource label

`init<S>(S, image: ImageResource, selection: Binding<SelectionValue>, content:
() -> Content)`

Creates a picker that generates its label from a string and image resource.

Available when `Label` is `Label<Text, Image>`, `SelectionValue` conforms to
`Hashable`, and `Content` conforms to `View`.

`init<C, S>(S, image: ImageResource, sources: C, selection: KeyPath<C.Element,
Binding<SelectionValue>>, content: () -> Content)`

Creates a picker bound to a collection of bindings that generates its label
from a string and image resource.

Available when `Label` is `Label<Text, Image>`, `SelectionValue` conforms to
`Hashable`, and `Content` conforms to `View`.

`init<C>(LocalizedStringKey, image: ImageResource, sources: C, selection:
KeyPath<C.Element, Binding<SelectionValue>>, content: () -> Content)`

Creates a picker that generates its label from a localized string key and
image resource.

Available when `Label` is `Label<Text, Image>`, `SelectionValue` conforms to
`Hashable`, and `Content` conforms to `View`.

Initializer

# init(_:image:sources:selection:content:)

Creates a picker bound to a collection of bindings that generates its label
from a string and image resource.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    init<C, S>(
        _ title: S,
        image: ImageResource,
        sources: C,
        selection: KeyPath<C.Element, Binding<SelectionValue>>,
        @ViewBuilder content: () -> Content
    ) where C : RandomAccessCollection, S : StringProtocol, C.Element == Binding<SelectionValue>

Available when `Label` is `Label<Text, Image>`, `SelectionValue` conforms to
`Hashable`, and `Content` conforms to `View`.

##  Parameters

`title`

    

A string that describes the purpose of selecting an option.

`image`

    

The name of the image resource to lookup.

`sources`

    

A collection of values used as the source for displaying the Picker’s
selection.

`selection`

    

The key path of the values that determines the currently-selected options.
When a user selects an option from the picker, the values at the key path of
all items in the `sources` collection are updated with the selected option.

`content`

    

A view that contains the set of options.

## Discussion

If the wrapped values of the collection passed to `sources` are not all the
same, some styles render the selection in a mixed state. The specific
presentation depends on the style. For example, a Picker with a menu style
uses dashes instead of checkmarks to indicate the selected values.

In the following example, a picker in a document inspector controls the
thickness of borders for the currently-selected shapes, which can be of any
number.

## See Also

### Creating a picker with an image resource label

`init<S>(S, image: ImageResource, selection: Binding<SelectionValue>, content:
() -> Content)`

Creates a picker that generates its label from a string and image resource.

Available when `Label` is `Label<Text, Image>`, `SelectionValue` conforms to
`Hashable`, and `Content` conforms to `View`.

`init(LocalizedStringKey, image: ImageResource, selection:
Binding<SelectionValue>, content: () -> Content)`

Creates a picker that generates its label from a localized string key and
image resource

Available when `Label` is `Label<Text, Image>`, `SelectionValue` conforms to
`Hashable`, and `Content` conforms to `View`.

`init<C>(LocalizedStringKey, image: ImageResource, sources: C, selection:
KeyPath<C.Element, Binding<SelectionValue>>, content: () -> Content)`

Creates a picker that generates its label from a localized string key and
image resource.

Available when `Label` is `Label<Text, Image>`, `SelectionValue` conforms to
`Hashable`, and `Content` conforms to `View`.

Initializer

# init(_:image:sources:selection:content:)

Creates a picker that generates its label from a localized string key and
image resource.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    init<C>(
        _ titleKey: LocalizedStringKey,
        image: ImageResource,
        sources: C,
        selection: KeyPath<C.Element, Binding<SelectionValue>>,
        @ViewBuilder content: () -> Content
    ) where C : RandomAccessCollection, C.Element == Binding<SelectionValue>

Available when `Label` is `Label<Text, Image>`, `SelectionValue` conforms to
`Hashable`, and `Content` conforms to `View`.

##  Parameters

`titleKey`

    

A localized string key that describes the purpose of selecting an option.

`image`

    

The name of the image resource to lookup.

`sources`

    

A collection of values used as the source for displaying he Picker’s
selection.

`selection`

    

The key path of the values that determines the currently-selected options.
When a user selects an option from the picker, the values at the key path of
all items in the `sources` collection are updated with the selected option.

`content`

    

A view that contains the set of options.

## Discussion

If the wrapped values of the collection passed to `sources` are not all the
same, some styles render the selection in a mixed state. The specific
presentation depends on the style. For example, a Picker with a menu style
uses dashes instead of checkmarks to indicate the selected values.

In the following example, a picker in a document inspector controls the
thickness of borders for the currently-selected shapes, which can be of any
number.

## See Also

### Creating a picker with an image resource label

`init<S>(S, image: ImageResource, selection: Binding<SelectionValue>, content:
() -> Content)`

Creates a picker that generates its label from a string and image resource.

Available when `Label` is `Label<Text, Image>`, `SelectionValue` conforms to
`Hashable`, and `Content` conforms to `View`.

`init(LocalizedStringKey, image: ImageResource, selection:
Binding<SelectionValue>, content: () -> Content)`

Creates a picker that generates its label from a localized string key and
image resource

Available when `Label` is `Label<Text, Image>`, `SelectionValue` conforms to
`Hashable`, and `Content` conforms to `View`.

`init<C, S>(S, image: ImageResource, sources: C, selection: KeyPath<C.Element,
Binding<SelectionValue>>, content: () -> Content)`

Creates a picker bound to a collection of bindings that generates its label
from a string and image resource.

Available when `Label` is `Label<Text, Image>`, `SelectionValue` conforms to
`Hashable`, and `Content` conforms to `View`.

Initializer

# init(_:systemImage:selection:content:)

Creates a picker that generates its label from a string and system image.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    init<S>(
        _ title: S,
        systemImage: String,
        selection: Binding<SelectionValue>,
        @ViewBuilder content: () -> Content
    ) where S : StringProtocol

Available when `Label` is `Label<Text, Image>`, `SelectionValue` conforms to
`Hashable`, and `Content` conforms to `View`.

##  Parameters

`title`

    

A string that describes the purpose of selecting an option.

`systemImage`

    

The name of the image resource to lookup.

`selection`

    

A binding to a property that determines the currently-selected option.

`content`

    

A view that contains the set of options.

## See Also

### Creating a picker with an system image label

`init(LocalizedStringKey, systemImage: String, selection:
Binding<SelectionValue>, content: () -> Content)`

Creates a picker that generates its label from a localized string key and
system image.

Available when `Label` is `Label<Text, Image>`, `SelectionValue` conforms to
`Hashable`, and `Content` conforms to `View`.

`init<C>(LocalizedStringKey, systemImage: String, sources: C, selection:
KeyPath<C.Element, Binding<SelectionValue>>, content: () -> Content)`

Creates a picker that generates its label from a localized string key.

Available when `Label` is `Label<Text, Image>`, `SelectionValue` conforms to
`Hashable`, and `Content` conforms to `View`.

`init<C, S>(S, systemImage: String, sources: C, selection: KeyPath<C.Element,
Binding<SelectionValue>>, content: () -> Content)`

Creates a picker bound to a collection of bindings that generates its label
from a string.

Available when `Label` is `Label<Text, Image>`, `SelectionValue` conforms to
`Hashable`, and `Content` conforms to `View`.

Initializer

# init(_:systemImage:selection:content:)

Creates a picker that generates its label from a localized string key and
system image.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    init(
        _ titleKey: LocalizedStringKey,
        systemImage: String,
        selection: Binding<SelectionValue>,
        @ViewBuilder content: () -> Content
    )

Available when `Label` is `Label<Text, Image>`, `SelectionValue` conforms to
`Hashable`, and `Content` conforms to `View`.

##  Parameters

`titleKey`

    

A localized string key that describes the purpose of selecting an option.

`systemImage`

    

The name of the image resource to lookup.

`selection`

    

A binding to a property that determines the currently-selected option.

`content`

    

A view that contains the set of options.

## Discussion

This initializer creates a `Text` view on your behalf, and treats the
localized key similar to `init(_:tableName:bundle:comment:)`. See `Text` for
more information about localizing strings.

To initialize a picker with a string variable, use
`init(_:selection:content:)` instead.

## See Also

### Creating a picker with an system image label

`init<S>(S, systemImage: String, selection: Binding<SelectionValue>, content:
() -> Content)`

Creates a picker that generates its label from a string and system image.

Available when `Label` is `Label<Text, Image>`, `SelectionValue` conforms to
`Hashable`, and `Content` conforms to `View`.

`init<C>(LocalizedStringKey, systemImage: String, sources: C, selection:
KeyPath<C.Element, Binding<SelectionValue>>, content: () -> Content)`

Creates a picker that generates its label from a localized string key.

Available when `Label` is `Label<Text, Image>`, `SelectionValue` conforms to
`Hashable`, and `Content` conforms to `View`.

`init<C, S>(S, systemImage: String, sources: C, selection: KeyPath<C.Element,
Binding<SelectionValue>>, content: () -> Content)`

Creates a picker bound to a collection of bindings that generates its label
from a string.

Available when `Label` is `Label<Text, Image>`, `SelectionValue` conforms to
`Hashable`, and `Content` conforms to `View`.

Initializer

# init(_:systemImage:sources:selection:content:)

Creates a picker that generates its label from a localized string key.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    init<C>(
        _ titleKey: LocalizedStringKey,
        systemImage: String,
        sources: C,
        selection: KeyPath<C.Element, Binding<SelectionValue>>,
        @ViewBuilder content: () -> Content
    ) where C : RandomAccessCollection, C.Element == Binding<SelectionValue>

Available when `Label` is `Label<Text, Image>`, `SelectionValue` conforms to
`Hashable`, and `Content` conforms to `View`.

##  Parameters

`titleKey`

    

A localized string key that describes the purpose of selecting an option.

`systemImage`

    

The name of the image resource to lookup.

`sources`

    

A collection of values used as the source for displaying the Picker’s
selection.

`selection`

    

The key path of the values that determines the currently-selected options.
When a user selects an option from the picker, the values at the key path of
all items in the `sources` collection are updated with the selected option.

`content`

    

A view that contains the set of options.

## Discussion

If the wrapped values of the collection passed to `sources` are not all the
same, some styles render the selection in a mixed state. The specific
presentation depends on the style. For example, a Picker with a menu style
uses dashes instead of checkmarks to indicate the selected values.

In the following example, a picker in a document inspector controls the
thickness of borders for the currently-selected shapes, which can be of any
number.

## See Also

### Creating a picker with an system image label

`init<S>(S, systemImage: String, selection: Binding<SelectionValue>, content:
() -> Content)`

Creates a picker that generates its label from a string and system image.

Available when `Label` is `Label<Text, Image>`, `SelectionValue` conforms to
`Hashable`, and `Content` conforms to `View`.

`init(LocalizedStringKey, systemImage: String, selection:
Binding<SelectionValue>, content: () -> Content)`

Creates a picker that generates its label from a localized string key and
system image.

Available when `Label` is `Label<Text, Image>`, `SelectionValue` conforms to
`Hashable`, and `Content` conforms to `View`.

`init<C, S>(S, systemImage: String, sources: C, selection: KeyPath<C.Element,
Binding<SelectionValue>>, content: () -> Content)`

Creates a picker bound to a collection of bindings that generates its label
from a string.

Available when `Label` is `Label<Text, Image>`, `SelectionValue` conforms to
`Hashable`, and `Content` conforms to `View`.

Initializer

# init(_:systemImage:sources:selection:content:)

Creates a picker bound to a collection of bindings that generates its label
from a string.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    init<C, S>(
        _ title: S,
        systemImage: String,
        sources: C,
        selection: KeyPath<C.Element, Binding<SelectionValue>>,
        @ViewBuilder content: () -> Content
    ) where C : RandomAccessCollection, S : StringProtocol, C.Element == Binding<SelectionValue>

Available when `Label` is `Label<Text, Image>`, `SelectionValue` conforms to
`Hashable`, and `Content` conforms to `View`.

##  Parameters

`title`

    

A string that describes the purpose of selecting an option.

`systemImage`

    

The name of the image resource to lookup.

`sources`

    

A collection of values used as the source for displaying the Picker’s
selection.

`selection`

    

The key path of the values that determines the currently-selected options.
When a user selects an option from the picker, the values at the key path of
all items in the `sources` collection are updated with the selected option.

`content`

    

A view that contains the set of options.

## Discussion

If the wrapped values of the collection passed to `sources` are not all the
same, some styles render the selection in a mixed state. The specific
presentation depends on the style. For example, a Picker with a menu style
uses dashes instead of checkmarks to indicate the selected values.

In the following example, a picker in a document inspector controls the
thickness of borders for the currently-selected shapes, which can be of any
number.

## See Also

### Creating a picker with an system image label

`init<S>(S, systemImage: String, selection: Binding<SelectionValue>, content:
() -> Content)`

Creates a picker that generates its label from a string and system image.

Available when `Label` is `Label<Text, Image>`, `SelectionValue` conforms to
`Hashable`, and `Content` conforms to `View`.

`init(LocalizedStringKey, systemImage: String, selection:
Binding<SelectionValue>, content: () -> Content)`

Creates a picker that generates its label from a localized string key and
system image.

Available when `Label` is `Label<Text, Image>`, `SelectionValue` conforms to
`Hashable`, and `Content` conforms to `View`.

`init<C>(LocalizedStringKey, systemImage: String, sources: C, selection:
KeyPath<C.Element, Binding<SelectionValue>>, content: () -> Content)`

Creates a picker that generates its label from a localized string key.

Available when `Label` is `Label<Text, Image>`, `SelectionValue` conforms to
`Hashable`, and `Content` conforms to `View`.

Initializer

# init(selection:label:content:)

Creates a picker that displays a custom label.

iOS 13.0–17.4  Deprecated  iPadOS 13.0–17.4  Deprecated  macOS 10.15–14.4
Deprecated  Mac Catalyst 13.0–17.4  Deprecated  tvOS 13.0–17.4  Deprecated
watchOS 6.0–10.4  Deprecated  visionOS 1.0+

    
    
    init(
        selection: Binding<SelectionValue>,
        label: Label,
        @ViewBuilder content: () -> Content
    )

Available when `Label` conforms to `View`, `SelectionValue` conforms to
`Hashable`, and `Content` conforms to `View`.

Deprecated

Use `init(selection:content:label:)` instead.

##  Parameters

`selection`

    

A binding to a property that determines the currently-selected option.

`label`

    

A view that describes the purpose of selecting an option.

`content`

    

A view that contains the set of options.

