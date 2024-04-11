Initializer

# init(content:)

Creates a window group.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    init(@ViewBuilder content: () -> Content)

##  Parameters

`content`

    

A closure that creates the content for each instance of the group.

## Discussion

The window group uses the given view as a template to form the content of each
window in the group.

## See Also

### Creating a window group

`init(Text, content: () -> Content)`

Creates a window group with a text view title.

`init(LocalizedStringKey, content: () -> Content)`

Creates a window group with a localized title string.

`init<S>(S, content: () -> Content)`

Creates a window group with a title string.

Initializer

# init(_:content:)

Creates a window group with a text view title.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    init(
        _ title: Text,
        @ViewBuilder content: () -> Content
    )

##  Parameters

`title`

    

The `Text` view to use for the group’s title.

`content`

    

A closure that creates the content for each instance of the group.

## Discussion

The window group uses the given view as a template to form the content of each
window in the group. The system uses the title to distinguish the window group
in the user interface, such as in the name of commands associated with the
group.

Important

The system ignores any text styling that you apply to the `Text` view title,
like bold or italics. However, you can use the formatting controls that the
view offers, like for localization, dates, and numerical representations.

## See Also

### Creating a window group

`init(content: () -> Content)`

Creates a window group.

`init(LocalizedStringKey, content: () -> Content)`

Creates a window group with a localized title string.

`init<S>(S, content: () -> Content)`

Creates a window group with a title string.

Initializer

# init(_:content:)

Creates a window group with a localized title string.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    init(
        _ titleKey: LocalizedStringKey,
        @ViewBuilder content: () -> Content
    )

##  Parameters

`titleKey`

    

The title key to use for the group’s title.

`content`

    

A closure that creates the content for each instance of the group.

## Discussion

The window group uses the specified content as a template to create each
window in the group. The system uses the title to distinguish the window group
in the user interface, such as in the name of commands associated with the
group.

## See Also

### Creating a window group

`init(content: () -> Content)`

Creates a window group.

`init(Text, content: () -> Content)`

Creates a window group with a text view title.

`init<S>(S, content: () -> Content)`

Creates a window group with a title string.

Initializer

# init(_:content:)

Creates a window group with a title string.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    init<S>(
        _ title: S,
        @ViewBuilder content: () -> Content
    ) where S : StringProtocol

##  Parameters

`title`

    

The string to use for the title of the group.

`content`

    

A closure that creates the content for each instance of the group.

## Discussion

The window group uses the specified content as a template to create each
window in the group. The system uses the title to distinguish the window group
in the user interface, such as in the name of commands associated with the
group.

## See Also

### Creating a window group

`init(content: () -> Content)`

Creates a window group.

`init(Text, content: () -> Content)`

Creates a window group with a text view title.

`init(LocalizedStringKey, content: () -> Content)`

Creates a window group with a localized title string.

Initializer

# init(id:content:)

Creates a window group with an identifier.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    init(
        id: String,
        @ViewBuilder content: () -> Content
    )

##  Parameters

`id`

    

A string that uniquely identifies the window group. Identifiers must be unique
among the window groups in your app.

`content`

    

A closure that creates the content for each instance of the group.

## Discussion

The window group uses the given view as a template to form the content of each
window in the group.

## See Also

### Identifying a window group

`init(Text, id: String, content: () -> Content)`

Creates a window group with a text view title and an identifier.

`init(LocalizedStringKey, id: String, content: () -> Content)`

Creates a window group with a localized title string and an identifier.

`init<S>(S, id: String, content: () -> Content)`

Creates a window group with a title string and an identifier.

Initializer

# init(_:id:content:)

Creates a window group with a text view title and an identifier.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    init(
        _ title: Text,
        id: String,
        @ViewBuilder content: () -> Content
    )

##  Parameters

`title`

    

The `Text` view to use for the group’s title.

`id`

    

A string that uniquely identifies the window group. Identifiers must be unique
among the window groups in your app.

`content`

    

A closure that creates the content for each instance of the group.

## Discussion

The window group uses the specified content as a template to create each
window in the group. The system uses the title to distinguish the window group
in the user interface, such as in the name of commands associated with the
group.

Important

The system ignores any text styling that you apply to the `Text` view title,
like bold or italics. However, you can use the formatting controls that the
view offers, like for localization, dates, and numerical representations.

## See Also

### Identifying a window group

`init(id: String, content: () -> Content)`

Creates a window group with an identifier.

`init(LocalizedStringKey, id: String, content: () -> Content)`

Creates a window group with a localized title string and an identifier.

`init<S>(S, id: String, content: () -> Content)`

Creates a window group with a title string and an identifier.

Initializer

# init(_:id:content:)

Creates a window group with a localized title string and an identifier.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    init(
        _ titleKey: LocalizedStringKey,
        id: String,
        @ViewBuilder content: () -> Content
    )

##  Parameters

`titleKey`

    

The title key to use for the title of the group.

`id`

    

A string that uniquely identifies the window group. Identifiers must be unique
among the window groups in your app.

`content`

    

A closure that creates the content for each instance of the group.

## Discussion

The window group uses the specified content as a template to create each
window in the group. The system uses the title to distinguish the window group
in the user interface, such as in the name of commands associated with the
group.

## See Also

### Identifying a window group

`init(id: String, content: () -> Content)`

Creates a window group with an identifier.

`init(Text, id: String, content: () -> Content)`

Creates a window group with a text view title and an identifier.

`init<S>(S, id: String, content: () -> Content)`

Creates a window group with a title string and an identifier.

Initializer

# init(_:id:content:)

Creates a window group with a title string and an identifier.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    init<S>(
        _ title: S,
        id: String,
        @ViewBuilder content: () -> Content
    ) where S : StringProtocol

##  Parameters

`title`

    

The string to use for the title of the group.

`id`

    

A string that uniquely identifies the window group. Identifiers must be unique
among the window groups in your app.

`content`

    

A closure that creates the content for each instance of the group.

## Discussion

The window group uses the specified content as a template to create each
window in the group. The system uses the title to distinguish the window group
in the user interface, such as in the name of commands associated with the
group.

## See Also

### Identifying a window group

`init(id: String, content: () -> Content)`

Creates a window group with an identifier.

`init(Text, id: String, content: () -> Content)`

Creates a window group with a text view title and an identifier.

`init(LocalizedStringKey, id: String, content: () -> Content)`

Creates a window group with a localized title string and an identifier.

Initializer

# init(for:content:)

Creates a data-presenting window group.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    init<D, C>(
        for type: D.Type,
        @ViewBuilder content: @escaping (Binding<D?>) -> C
    ) where Content == PresentedWindowContent<D, C>, D : Decodable, D : Encodable, D : Hashable, C : View

Available when `Content` conforms to `View`.

##  Parameters

`type`

    

The type of presented data this window group accepts.

`content`

    

A closure that creates the content for each instance of the group. The closure
receives a binding to the value that you pass into the `openWindow` action
when you open the window. SwiftUI automatically persists and restores the
value of this binding as part of the state restoration process.

## Discussion

The window group uses the given view as a template to form the content of each
window in the group.

SwiftUI creates a window from the group when you present a value of the
specified type using the `openWindow` action.

## See Also

### Creating a data-driven window group

`init<D, C>(LocalizedStringKey, for: D.Type, content: (Binding<D?>) -> C)`

Creates a data-presenting window group with a localized title string.

Available when `Content` conforms to `View`.

`init<S, D, C>(S, for: D.Type, content: (Binding<D?>) -> C)`

Creates a data-presenting window group with a title string.

Available when `Content` conforms to `View`.

`init<D, C>(Text, for: D.Type, content: (Binding<D?>) -> C)`

Creates a data-presenting window group with a text view title.

Available when `Content` conforms to `View`.

Initializer

# init(_:for:content:)

Creates a data-presenting window group with a localized title string.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    init<D, C>(
        _ titleKey: LocalizedStringKey,
        for type: D.Type,
        @ViewBuilder content: @escaping (Binding<D?>) -> C
    ) where Content == PresentedWindowContent<D, C>, D : Decodable, D : Encodable, D : Hashable, C : View

Available when `Content` conforms to `View`.

##  Parameters

`titleKey`

    

The title key to use for the group’s title.

`type`

    

The type of presented data this window group accepts.

`content`

    

A closure that creates the content for each instance of the group. The closure
receives a binding to the value that you pass into the `openWindow` action
when you open the window. SwiftUI automatically persists and restores the
value of this binding as part of the state restoration process.

## Discussion

The window group uses the specified content as a template to create each
window in the group.

The system uses the title to distinguish the window group in the user
interface, such as in the name of commands associated with the group.

SwiftUI creates a window from the group when you present a value of the
specified type using the `openWindow` action.

## See Also

### Creating a data-driven window group

`init<D, C>(for: D.Type, content: (Binding<D?>) -> C)`

Creates a data-presenting window group.

Available when `Content` conforms to `View`.

`init<S, D, C>(S, for: D.Type, content: (Binding<D?>) -> C)`

Creates a data-presenting window group with a title string.

Available when `Content` conforms to `View`.

`init<D, C>(Text, for: D.Type, content: (Binding<D?>) -> C)`

Creates a data-presenting window group with a text view title.

Available when `Content` conforms to `View`.

Initializer

# init(_:for:content:)

Creates a data-presenting window group with a title string.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    init<S, D, C>(
        _ title: S,
        for type: D.Type,
        @ViewBuilder content: @escaping (Binding<D?>) -> C
    ) where Content == PresentedWindowContent<D, C>, S : StringProtocol, D : Decodable, D : Encodable, D : Hashable, C : View

Available when `Content` conforms to `View`.

##  Parameters

`title`

    

The string to use for the title of the group.

`type`

    

The type of presented data this window group accepts.

`content`

    

A closure that creates the content for each instance of the group. The closure
receives a binding to the value that you pass into the `openWindow` action
when you open the window. SwiftUI automatically persists and restores the
value of this binding as part of the state restoration process.

## Discussion

The window group uses the specified content as a template to create each
window in the group.

The system uses the title to distinguish the window group in the user
interface, such as in the name of commands associated with the group.

SwiftUI creates a window from the group when you present a value of the
specified type using the `openWindow` action.

## See Also

### Creating a data-driven window group

`init<D, C>(for: D.Type, content: (Binding<D?>) -> C)`

Creates a data-presenting window group.

Available when `Content` conforms to `View`.

`init<D, C>(LocalizedStringKey, for: D.Type, content: (Binding<D?>) -> C)`

Creates a data-presenting window group with a localized title string.

Available when `Content` conforms to `View`.

`init<D, C>(Text, for: D.Type, content: (Binding<D?>) -> C)`

Creates a data-presenting window group with a text view title.

Available when `Content` conforms to `View`.

Initializer

# init(_:for:content:)

Creates a data-presenting window group with a text view title.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    init<D, C>(
        _ title: Text,
        for type: D.Type,
        @ViewBuilder content: @escaping (Binding<D?>) -> C
    ) where Content == PresentedWindowContent<D, C>, D : Decodable, D : Encodable, D : Hashable, C : View

Available when `Content` conforms to `View`.

##  Parameters

`title`

    

The `Text` view to use for the group’s title.

`type`

    

The type of presented data this window group accepts.

`content`

    

A closure that creates the content for each instance of the group. The closure
receives a binding to the value that you pass into the `openWindow` action
when you open the window. SwiftUI automatically persists and restores the
value of this binding as part of the state restoration process.

## Discussion

The window group uses the given view as a template to form the content of each
window in the group.

The system uses the title to distinguish the window group in the user
interface, such as in the name of commands associated with the group.

Important

The system ignores any text styling that you apply to the `Text` view title,
like bold or italics. However, you can use the formatting controls that the
view offers, like for localization, dates, and numerical representations.

SwiftUI creates a window from the group when you present a value of the
specified type using the `openWindow` action.

## See Also

### Creating a data-driven window group

`init<D, C>(for: D.Type, content: (Binding<D?>) -> C)`

Creates a data-presenting window group.

Available when `Content` conforms to `View`.

`init<D, C>(LocalizedStringKey, for: D.Type, content: (Binding<D?>) -> C)`

Creates a data-presenting window group with a localized title string.

Available when `Content` conforms to `View`.

`init<S, D, C>(S, for: D.Type, content: (Binding<D?>) -> C)`

Creates a data-presenting window group with a title string.

Available when `Content` conforms to `View`.

Initializer

# init(for:content:defaultValue:)

Creates a data-presenting window group with a default value.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    init<D, C>(
        for type: D.Type = D.self,
        @ViewBuilder content: @escaping (Binding<D>) -> C,
        defaultValue: @escaping () -> D
    ) where Content == PresentedWindowContent<D, C>, D : Decodable, D : Encodable, D : Hashable, C : View

Available when `Content` conforms to `View`.

##  Parameters

`type`

    

The type of presented data this window group accepts.

`content`

    

A closure that creates the content for each instance of the group. The closure
receives a binding to the value that you pass into the `openWindow` action
when you open the window. SwiftUI automatically persists and restores the
value of this binding as part of the state restoration process.

`defaultValue`

    

A closure that returns a default value to present. SwiftUI calls this closure
when it has no data to provide, like when someone opens a new window from the
File > New Window menu item.

## Discussion

The window group using the given view as a template to form the content of
each window in the group.

SwiftUI creates a window from the group when you present a value of the
specified type using the `openWindow` action.

## See Also

### Providing default data to a window group

`init<D, C>(LocalizedStringKey, for: D.Type, content: (Binding<D>) -> C,
defaultValue: () -> D)`

Creates a data-presenting window group with a localized title string and a
default value.

Available when `Content` conforms to `View`.

`init<S, D, C>(S, for: D.Type, content: (Binding<D>) -> C, defaultValue: () ->
D)`

Creates a data-presenting window group with a title string and a default
value.

Available when `Content` conforms to `View`.

`init<D, C>(Text, for: D.Type, content: (Binding<D>) -> C, defaultValue: () ->
D)`

Creates a data-presenting window group with a text view title and a default
value.

Available when `Content` conforms to `View`.

Initializer

# init(_:for:content:defaultValue:)

Creates a data-presenting window group with a localized title string and a
default value.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    init<D, C>(
        _ titleKey: LocalizedStringKey,
        for type: D.Type = D.self,
        @ViewBuilder content: @escaping (Binding<D>) -> C,
        defaultValue: @escaping () -> D
    ) where Content == PresentedWindowContent<D, C>, D : Decodable, D : Encodable, D : Hashable, C : View

Available when `Content` conforms to `View`.

##  Parameters

`titleKey`

    

The title key to use for the group’s title.

`type`

    

The type of presented data this window group accepts.

`content`

    

A closure that creates the content for each instance of the group. The closure
receives a binding to the value that you pass into the `openWindow` action
when you open the window. SwiftUI automatically persists and restores the
value of this binding as part of the state restoration process.

`defaultValue`

    

A closure that returns a default value to present. SwiftUI calls this closure
when it has no data to provide, like when someone opens a new window from the
File > New Window menu item.

## Discussion

The window group uses the specified content as a template to create each
window in the group.

The system uses the title to distinguish the window group in the user
interface, such as in the name of commands associated with the group.

SwiftUI creates a window from the group when you present a value of the
specified type using the `openWindow` action.

## See Also

### Providing default data to a window group

`init<D, C>(for: D.Type, content: (Binding<D>) -> C, defaultValue: () -> D)`

Creates a data-presenting window group with a default value.

Available when `Content` conforms to `View`.

`init<S, D, C>(S, for: D.Type, content: (Binding<D>) -> C, defaultValue: () ->
D)`

Creates a data-presenting window group with a title string and a default
value.

Available when `Content` conforms to `View`.

`init<D, C>(Text, for: D.Type, content: (Binding<D>) -> C, defaultValue: () ->
D)`

Creates a data-presenting window group with a text view title and a default
value.

Available when `Content` conforms to `View`.

Initializer

# init(_:for:content:defaultValue:)

Creates a data-presenting window group with a title string and a default
value.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    init<S, D, C>(
        _ title: S,
        for type: D.Type = D.self,
        @ViewBuilder content: @escaping (Binding<D>) -> C,
        defaultValue: @escaping () -> D
    ) where Content == PresentedWindowContent<D, C>, S : StringProtocol, D : Decodable, D : Encodable, D : Hashable, C : View

Available when `Content` conforms to `View`.

##  Parameters

`title`

    

The string to use for the title of the group.

`type`

    

The type of presented data this window group accepts.

`content`

    

A closure that creates the content for each instance of the group. The closure
receives a binding to the value that you pass into the `openWindow` action
when you open the window. SwiftUI automatically persists and restores the
value of this binding as part of the state restoration process.

`defaultValue`

    

A closure that returns a default value to present. SwiftUI calls this closure
when it has no data to provide, like when someone opens a new window from the
File > New Window menu item.

## Discussion

The window group uses the specified content as a template to create each
window in the group.

The system uses the title to distinguish the window group in the user
interface, such as in the name of commands associated with the group.

SwiftUI creates a window from the group when you present a value of the
specified type using the `openWindow` action.

## See Also

### Providing default data to a window group

`init<D, C>(for: D.Type, content: (Binding<D>) -> C, defaultValue: () -> D)`

Creates a data-presenting window group with a default value.

Available when `Content` conforms to `View`.

`init<D, C>(LocalizedStringKey, for: D.Type, content: (Binding<D>) -> C,
defaultValue: () -> D)`

Creates a data-presenting window group with a localized title string and a
default value.

Available when `Content` conforms to `View`.

`init<D, C>(Text, for: D.Type, content: (Binding<D>) -> C, defaultValue: () ->
D)`

Creates a data-presenting window group with a text view title and a default
value.

Available when `Content` conforms to `View`.

Initializer

# init(_:for:content:defaultValue:)

Creates a data-presenting window group with a text view title and a default
value.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    init<D, C>(
        _ title: Text,
        for type: D.Type = D.self,
        @ViewBuilder content: @escaping (Binding<D>) -> C,
        defaultValue: @escaping () -> D
    ) where Content == PresentedWindowContent<D, C>, D : Decodable, D : Encodable, D : Hashable, C : View

Available when `Content` conforms to `View`.

##  Parameters

`title`

    

The `Text` view to use for the group’s title.

`type`

    

The type of presented data this window group accepts.

`content`

    

A closure that creates the content for each instance of the group. The closure
receives a binding to the value that you pass into the `openWindow` action
when you open the window. SwiftUI automatically persists and restores the
value of this binding as part of the state restoration process.

`defaultValue`

    

A closure that returns a default value to present. SwiftUI calls this closure
when it has no data to provide, like when someone opens a new window from the
File > New Window menu item.

## Discussion

The window group uses the given view as a template to form the content of each
window in the group.

The system uses the title to distinguish the window group in the user
interface, such as in the name of commands associated with the group.

Important

The system ignores any text styling that you apply to the `Text` view title,
like bold or italics. However, you can use the formatting controls that the
view offers, like for localization, dates, and numerical representations.

SwiftUI creates a window from the group when you present a value of the
specified type using the `openWindow` action.

## See Also

### Providing default data to a window group

`init<D, C>(for: D.Type, content: (Binding<D>) -> C, defaultValue: () -> D)`

Creates a data-presenting window group with a default value.

Available when `Content` conforms to `View`.

`init<D, C>(LocalizedStringKey, for: D.Type, content: (Binding<D>) -> C,
defaultValue: () -> D)`

Creates a data-presenting window group with a localized title string and a
default value.

Available when `Content` conforms to `View`.

`init<S, D, C>(S, for: D.Type, content: (Binding<D>) -> C, defaultValue: () ->
D)`

Creates a data-presenting window group with a title string and a default
value.

Available when `Content` conforms to `View`.

Initializer

# init(id:for:content:)

Creates a data-presenting window group with an identifier.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    init<D, C>(
        id: String,
        for type: D.Type,
        @ViewBuilder content: @escaping (Binding<D?>) -> C
    ) where Content == PresentedWindowContent<D, C>, D : Decodable, D : Encodable, D : Hashable, C : View

Available when `Content` conforms to `View`.

##  Parameters

`id`

    

A string that uniquely identifies the window group. Identifiers must be unique
among the window groups in your app.

`type`

    

The type of presented data this window group accepts.

`content`

    

A closure that creates the content for each instance of the group. The closure
receives a binding to the value that you pass into the `openWindow` action
when you open the window. SwiftUI automatically persists and restores the
value of this binding as part of the state restoration process.

## Discussion

The window group uses the specified content as a template to create each
window in the group.

SwiftUI creates a window from the group when you present a value of the
specified type using the `openWindow` action.

## See Also

### Identifying a data-driven window group

`init<D, C>(LocalizedStringKey, id: String, for: D.Type, content:
(Binding<D?>) -> C)`

Creates a data-presenting window group with a localized title string and an
identifier.

Available when `Content` conforms to `View`.

`init<S, D, C>(S, id: String, for: D.Type, content: (Binding<D?>) -> C)`

Creates a data-presenting window group with a title string and an identifier.

Available when `Content` conforms to `View`.

`init<D, C>(Text, id: String, for: D.Type, content: (Binding<D?>) -> C)`

Creates a data-presenting window group with a text view title and an
identifier.

Available when `Content` conforms to `View`.

Initializer

# init(_:id:for:content:)

Creates a data-presenting window group with a localized title string and an
identifier.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    init<D, C>(
        _ titleKey: LocalizedStringKey,
        id: String,
        for type: D.Type,
        @ViewBuilder content: @escaping (Binding<D?>) -> C
    ) where Content == PresentedWindowContent<D, C>, D : Decodable, D : Encodable, D : Hashable, C : View

Available when `Content` conforms to `View`.

##  Parameters

`titleKey`

    

The title key to use for the group’s title.

`id`

    

A string that uniquely identifies the window group. Identifiers must be unique
among the window groups in your app.

`type`

    

The type of presented data this window group accepts.

`content`

    

A closure that creates the content for each instance of the group. The closure
receives a binding to the value that you pass into the `openWindow` action
when you open the window. SwiftUI automatically persists and restores the
value of this binding as part of the state restoration process.

## Discussion

The window group uses the specified content as a template to create each
window in the group.

The system uses the title to distinguish the window group in the user
interface, such as in the name of commands associated with the group.

SwiftUI creates a window from the group when you present a value of the
specified type using the `openWindow` action.

## See Also

### Identifying a data-driven window group

`init<D, C>(id: String, for: D.Type, content: (Binding<D?>) -> C)`

Creates a data-presenting window group with an identifier.

Available when `Content` conforms to `View`.

`init<S, D, C>(S, id: String, for: D.Type, content: (Binding<D?>) -> C)`

Creates a data-presenting window group with a title string and an identifier.

Available when `Content` conforms to `View`.

`init<D, C>(Text, id: String, for: D.Type, content: (Binding<D?>) -> C)`

Creates a data-presenting window group with a text view title and an
identifier.

Available when `Content` conforms to `View`.

Initializer

# init(_:id:for:content:)

Creates a data-presenting window group with a title string and an identifier.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    init<S, D, C>(
        _ title: S,
        id: String,
        for type: D.Type,
        @ViewBuilder content: @escaping (Binding<D?>) -> C
    ) where Content == PresentedWindowContent<D, C>, S : StringProtocol, D : Decodable, D : Encodable, D : Hashable, C : View

Available when `Content` conforms to `View`.

##  Parameters

`title`

    

The string to use for the title of the group.

`id`

    

A string that uniquely identifies the window group. Identifiers must be unique
among the window groups in your app.

`type`

    

The type of presented data this window group accepts.

`content`

    

A closure that creates the content for each instance of the group. The closure
receives a binding to the value that you pass into the `openWindow` action
when you open the window. SwiftUI automatically persists and restores the
value of this binding as part of the state restoration process.

## Discussion

The window group uses the specified content as a template to create each
window in the group.

The system uses the title to distinguish the window group in the user
interface, such as in the name of commands associated with the group.

SwiftUI creates a window from the group when you present a value of the
specified type using the `openWindow` action.

## See Also

### Identifying a data-driven window group

`init<D, C>(id: String, for: D.Type, content: (Binding<D?>) -> C)`

Creates a data-presenting window group with an identifier.

Available when `Content` conforms to `View`.

`init<D, C>(LocalizedStringKey, id: String, for: D.Type, content:
(Binding<D?>) -> C)`

Creates a data-presenting window group with a localized title string and an
identifier.

Available when `Content` conforms to `View`.

`init<D, C>(Text, id: String, for: D.Type, content: (Binding<D?>) -> C)`

Creates a data-presenting window group with a text view title and an
identifier.

Available when `Content` conforms to `View`.

Initializer

# init(_:id:for:content:)

Creates a data-presenting window group with a text view title and an
identifier.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    init<D, C>(
        _ title: Text,
        id: String,
        for type: D.Type,
        @ViewBuilder content: @escaping (Binding<D?>) -> C
    ) where Content == PresentedWindowContent<D, C>, D : Decodable, D : Encodable, D : Hashable, C : View

Available when `Content` conforms to `View`.

##  Parameters

`title`

    

The `Text` view to use for the group’s title.

`id`

    

A string that uniquely identifies the window group. Identifiers must be unique
among the window groups in your app.

`type`

    

The type of presented data this window group accepts.

`content`

    

A closure that creates the content for each instance of the group. The closure
receives a binding to the value that you pass into the `openWindow` action
when you open the window. SwiftUI automatically persists and restores the
value of this binding as part of the state restoration process.

## Discussion

The window group uses the specified content as a template to create each
window in the group.

The system uses the title to distinguish the window group in the user
interface, such as in the name of commands associated with the group.

Important

The system ignores any text styling that you apply to the `Text` view title,
like bold or italics. However, you can use the formatting controls that the
view offers, like for localization, dates, and numerical representations.

SwiftUI creates a window from the group when you present a value of the
specified type using the `openWindow` action.

## See Also

### Identifying a data-driven window group

`init<D, C>(id: String, for: D.Type, content: (Binding<D?>) -> C)`

Creates a data-presenting window group with an identifier.

Available when `Content` conforms to `View`.

`init<D, C>(LocalizedStringKey, id: String, for: D.Type, content:
(Binding<D?>) -> C)`

Creates a data-presenting window group with a localized title string and an
identifier.

Available when `Content` conforms to `View`.

`init<S, D, C>(S, id: String, for: D.Type, content: (Binding<D?>) -> C)`

Creates a data-presenting window group with a title string and an identifier.

Available when `Content` conforms to `View`.

Initializer

# init(id:for:content:defaultValue:)

Creates a data-presenting window group with an identifier and a default value.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    init<D, C>(
        id: String,
        for type: D.Type = D.self,
        @ViewBuilder content: @escaping (Binding<D>) -> C,
        defaultValue: @escaping () -> D
    ) where Content == PresentedWindowContent<D, C>, D : Decodable, D : Encodable, D : Hashable, C : View

Available when `Content` conforms to `View`.

##  Parameters

`id`

    

A string that uniquely identifies the window group. Identifiers must be unique
among the window groups in your app.

`type`

    

The type of presented data this window group accepts.

`content`

    

A closure that creates the content for each instance of the group. The closure
receives a binding to the value that you pass into the `openWindow` action
when you open the window. SwiftUI automatically persists and restores the
value of this binding as part of the state restoration process.

`defaultValue`

    

A closure that returns a default value to present. SwiftUI calls this closure
when it has no data to provide, like when someone opens a new window from the
File > New Window menu item.

## Discussion

The window group uses the given view as a template to form the content of each
window in the group.

SwiftUI creates a window from the group when you present a value of the
specified type using the `openWindow` action.

## See Also

### Identifying a window group that has default data

`init<D, C>(LocalizedStringKey, id: String, for: D.Type, content: (Binding<D>)
-> C, defaultValue: () -> D)`

Creates a data-presenting window group with a localized title string, an
identifier, and a default value.

Available when `Content` conforms to `View`.

`init<S, D, C>(S, id: String, for: D.Type, content: (Binding<D>) -> C,
defaultValue: () -> D)`

Creates a data-presenting window group with a title string, an identifier, and
a default value.

Available when `Content` conforms to `View`.

`init<D, C>(Text, id: String, for: D.Type, content: (Binding<D>) -> C,
defaultValue: () -> D)`

Creates a data-presenting window group with a text view title, an identifier,
and a default value.

Available when `Content` conforms to `View`.

Initializer

# init(_:id:for:content:defaultValue:)

Creates a data-presenting window group with a localized title string, an
identifier, and a default value.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    init<D, C>(
        _ titleKey: LocalizedStringKey,
        id: String,
        for type: D.Type = D.self,
        @ViewBuilder content: @escaping (Binding<D>) -> C,
        defaultValue: @escaping () -> D
    ) where Content == PresentedWindowContent<D, C>, D : Decodable, D : Encodable, D : Hashable, C : View

Available when `Content` conforms to `View`.

##  Parameters

`titleKey`

    

The title key to use for the group’s title.

`id`

    

A string that uniquely identifies the window group. Identifiers must be unique
among the window groups in your app.

`type`

    

The type of presented data this window group accepts.

`content`

    

A closure that creates the content for each instance of the group. The closure
receives a binding to the value that you pass into the `openWindow` action
when you open the window. SwiftUI automatically persists and restores the
value of this binding as part of the state restoration process.

`defaultValue`

    

A closure that returns a default value to present. SwiftUI calls this closure
when it has no data to provide, like when someone opens a new window from the
File > New Window menu item.

## Discussion

The window group uses the specified content as a template to create each
window in the group.

The system uses the title to distinguish the window group in the user
interface, such as in the name of commands associated with the group.

SwiftUI creates a window from the group when you present a value of the
specified type using the `openWindow` action.

## See Also

### Identifying a window group that has default data

`init<D, C>(id: String, for: D.Type, content: (Binding<D>) -> C, defaultValue:
() -> D)`

Creates a data-presenting window group with an identifier and a default value.

Available when `Content` conforms to `View`.

`init<S, D, C>(S, id: String, for: D.Type, content: (Binding<D>) -> C,
defaultValue: () -> D)`

Creates a data-presenting window group with a title string, an identifier, and
a default value.

Available when `Content` conforms to `View`.

`init<D, C>(Text, id: String, for: D.Type, content: (Binding<D>) -> C,
defaultValue: () -> D)`

Creates a data-presenting window group with a text view title, an identifier,
and a default value.

Available when `Content` conforms to `View`.

Initializer

# init(_:id:for:content:defaultValue:)

Creates a data-presenting window group with a title string, an identifier, and
a default value.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    init<S, D, C>(
        _ title: S,
        id: String,
        for type: D.Type = D.self,
        @ViewBuilder content: @escaping (Binding<D>) -> C,
        defaultValue: @escaping () -> D
    ) where Content == PresentedWindowContent<D, C>, S : StringProtocol, D : Decodable, D : Encodable, D : Hashable, C : View

Available when `Content` conforms to `View`.

##  Parameters

`title`

    

The string to use for the title of the group.

`id`

    

A string that uniquely identifies the window group. Identifiers must be unique
among the window groups in your app.

`type`

    

The type of presented data this window group accepts.

`content`

    

A closure that creates the content for each instance of the group. The closure
receives a binding to the value that you pass into the `openWindow` action
when you open the window. SwiftUI automatically persists and restores the
value of this binding as part of the state restoration process.

`defaultValue`

    

A closure that returns a default value to present. SwiftUI calls this closure
when it has no data to provide, like when someone opens a new window from the
File > New Window menu item.

## Discussion

The window group uses the specified content as a template to create each
window in the group.

The system uses the title to distinguish the window group in the user
interface, such as in the name of commands associated with the group.

SwiftUI creates a window from the group when you present a value of the
specified type using the `openWindow` action.

## See Also

### Identifying a window group that has default data

`init<D, C>(id: String, for: D.Type, content: (Binding<D>) -> C, defaultValue:
() -> D)`

Creates a data-presenting window group with an identifier and a default value.

Available when `Content` conforms to `View`.

`init<D, C>(LocalizedStringKey, id: String, for: D.Type, content: (Binding<D>)
-> C, defaultValue: () -> D)`

Creates a data-presenting window group with a localized title string, an
identifier, and a default value.

Available when `Content` conforms to `View`.

`init<D, C>(Text, id: String, for: D.Type, content: (Binding<D>) -> C,
defaultValue: () -> D)`

Creates a data-presenting window group with a text view title, an identifier,
and a default value.

Available when `Content` conforms to `View`.

Initializer

# init(_:id:for:content:defaultValue:)

Creates a data-presenting window group with a text view title, an identifier,
and a default value.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    init<D, C>(
        _ title: Text,
        id: String,
        for type: D.Type = D.self,
        @ViewBuilder content: @escaping (Binding<D>) -> C,
        defaultValue: @escaping () -> D
    ) where Content == PresentedWindowContent<D, C>, D : Decodable, D : Encodable, D : Hashable, C : View

Available when `Content` conforms to `View`.

##  Parameters

`title`

    

The `Text` view to use for the group’s title.

`id`

    

A string that uniquely identifies the window group. Identifiers must be unique
among the window groups in your app.

`type`

    

The type of presented data this window group accepts.

`content`

    

A closure that creates the content for each instance of the group. The closure
receives a binding to the value that you pass into the `openWindow` action
when you open the window. SwiftUI automatically persists and restores the
value of this binding as part of the state restoration process.

`defaultValue`

    

A closure that returns a default value to present. SwiftUI calls this closure
when it has no data to provide, like when someone opens a new window from the
File > New Window menu item.

## Discussion

The window group uses the specified content as a template to create each
window in the group.

The system uses the title to distinguish the window group in the user
interface, such as in the name of commands associated with the group.

Important

The system ignores any text styling that you apply to the `Text` view title,
like bold or italics. However, you can use the formatting controls that the
view offers, like for localization, dates, and numerical representations.

SwiftUI creates a window from the group when you present a value of the
specified type using the `openWindow` action.

## See Also

### Identifying a window group that has default data

`init<D, C>(id: String, for: D.Type, content: (Binding<D>) -> C, defaultValue:
() -> D)`

Creates a data-presenting window group with an identifier and a default value.

Available when `Content` conforms to `View`.

`init<D, C>(LocalizedStringKey, id: String, for: D.Type, content: (Binding<D>)
-> C, defaultValue: () -> D)`

Creates a data-presenting window group with a localized title string, an
identifier, and a default value.

Available when `Content` conforms to `View`.

`init<S, D, C>(S, id: String, for: D.Type, content: (Binding<D>) -> C,
defaultValue: () -> D)`

Creates a data-presenting window group with a title string, an identifier, and
a default value.

Available when `Content` conforms to `View`.

Structure

# PresentedWindowContent

A view that represents the content of a presented window.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    struct PresentedWindowContent<Data, Content> where Data : Decodable, Data : Encodable, Data : Hashable, Content : View

## Overview

You don’t create this type directly. `WindowGroup` creates values for you.

## Relationships

### Conforms To

  * `View`

