Initializer

# init(for:content:)

Creates the immersive space for a specified type of presented data.

visionOS 1.0+

    
    
    init(
        for type: Data.Type,
        @ImmersiveSpaceContentBuilder content: @escaping (Binding<Data?>) -> Content
    )

##  Parameters

`type`

    

The type of presented data this immersive space accepts.

`content`

    

An immersive space content builder that defines the content for each instance
of the immersive space. The closure receives a binding to the value that you
pass to the `openImmersiveSpace` action when you call that action to open an
immersive space. The system automatically persists and restores the value of
this binding during state restoration.

## Discussion

The space uses the specified content builder to form the content. Your app
invokes this initializer when it presents a value of the specified `type`
using the `openImmersiveSpace` action.

## See Also

### Creating a data-driven immersive space

`init<V>(for: Data.Type, content: (Binding<Data?>) -> V)`

Creates the immersive space for a specified type of presented data using view-
based content.

Available when `Content` conforms to `ImmersiveSpaceContent`, `Data` conforms
to `Decodable`, `Data` conforms to `Encodable`, and `Data` conforms to
`Hashable`.

`init(id: String, for: Data.Type, content: (Binding<Data?>) -> Content)`

Creates the immersive space associated with an identifier for a specified type
of presented data.

`init<V>(id: String, for: Data.Type, content: (Binding<Data?>) -> V)`

Creates the immersive space associated with an identifier for a specified type
of presented data using view-based content.

Available when `Content` conforms to `ImmersiveSpaceContent`, `Data` conforms
to `Decodable`, `Data` conforms to `Encodable`, and `Data` conforms to
`Hashable`.

Initializer

# init(for:content:)

Creates the immersive space for a specified type of presented data using view-
based content.

visionOS 1.0+

    
    
    init<V>(
        for type: Data.Type,
        @ViewBuilder content: @escaping (Binding<Data?>) -> V
    ) where Content == ImmersiveSpaceViewContent<V>, V : View

Available when `Content` conforms to `ImmersiveSpaceContent`, `Data` conforms
to `Decodable`, `Data` conforms to `Encodable`, and `Data` conforms to
`Hashable`.

##  Parameters

`type`

    

The type of presented data this immersive space accepts.

`content`

    

A view builder that defines the content for each instance of the immersive
space. The closure receives a binding to the value that you pass to the
`openImmersiveSpace` action when you use it to open an immersive space. The
system automatically persists and restores the value of this binding during
state restoration.

## Discussion

The immersive space uses the specified view as a template to form the content
of the space. Your app invokes this initializer when it presents a value of
the specified `type` using the `openImmersiveSpace` action.

## See Also

### Creating a data-driven immersive space

`init(for: Data.Type, content: (Binding<Data?>) -> Content)`

Creates the immersive space for a specified type of presented data.

`init(id: String, for: Data.Type, content: (Binding<Data?>) -> Content)`

Creates the immersive space associated with an identifier for a specified type
of presented data.

`init<V>(id: String, for: Data.Type, content: (Binding<Data?>) -> V)`

Creates the immersive space associated with an identifier for a specified type
of presented data using view-based content.

Available when `Content` conforms to `ImmersiveSpaceContent`, `Data` conforms
to `Decodable`, `Data` conforms to `Encodable`, and `Data` conforms to
`Hashable`.

Initializer

# init(id:for:content:)

Creates the immersive space associated with an identifier for a specified type
of presented data.

visionOS 1.0+

    
    
    init(
        id: String,
        for type: Data.Type,
        @ImmersiveSpaceContentBuilder content: @escaping (Binding<Data?>) -> Content
    )

##  Parameters

`id`

    

A string that uniquely identifies the immersive space. Ensure that identifiers
are unique among the immersive spaces in your app.

`type`

    

The type of presented data this immersive space accepts.

`content`

    

An immersive space content builder that defines the content for each instance
of the immersive space. The closure receives a binding to the value that you
pass to the `openImmersiveSpace` action when you call that action to open an
immersive space. The system automatically persists and restores the value of
this binding during state restoration.

## Discussion

The space uses the specified content builder to form the content. Your app
invokes this initializer when it presents a value of the specified `type`
using the `openImmersiveSpace` action.

## See Also

### Creating a data-driven immersive space

`init(for: Data.Type, content: (Binding<Data?>) -> Content)`

Creates the immersive space for a specified type of presented data.

`init<V>(for: Data.Type, content: (Binding<Data?>) -> V)`

Creates the immersive space for a specified type of presented data using view-
based content.

Available when `Content` conforms to `ImmersiveSpaceContent`, `Data` conforms
to `Decodable`, `Data` conforms to `Encodable`, and `Data` conforms to
`Hashable`.

`init<V>(id: String, for: Data.Type, content: (Binding<Data?>) -> V)`

Creates the immersive space associated with an identifier for a specified type
of presented data using view-based content.

Available when `Content` conforms to `ImmersiveSpaceContent`, `Data` conforms
to `Decodable`, `Data` conforms to `Encodable`, and `Data` conforms to
`Hashable`.

Initializer

# init(id:for:content:)

Creates the immersive space associated with an identifier for a specified type
of presented data using view-based content.

visionOS 1.0+

    
    
    init<V>(
        id: String,
        for type: Data.Type,
        @ViewBuilder content: @escaping (Binding<Data?>) -> V
    ) where Content == ImmersiveSpaceViewContent<V>, V : View

Available when `Content` conforms to `ImmersiveSpaceContent`, `Data` conforms
to `Decodable`, `Data` conforms to `Encodable`, and `Data` conforms to
`Hashable`.

##  Parameters

`id`

    

A string that uniquely identifies the immersive space. Ensure that identifiers
are unique among the immersive spaces in your app.

`type`

    

The type of presented data this immersive space accepts.

`content`

    

A view builder that defines the content for each instance of the immersive
space. The closure receives a binding to the value that you pass to the
`openImmersiveSpace` action when you use it to open an immersive space. The
system automatically persists and restores the value of this binding during
state restoration.

## Discussion

The immersive space uses the specified view as a template to form the content
of the space. Your app invokes this initializer when it presents a value of
the specified `type` using the `openImmersiveSpace` action.

## See Also

### Creating a data-driven immersive space

`init(for: Data.Type, content: (Binding<Data?>) -> Content)`

Creates the immersive space for a specified type of presented data.

`init<V>(for: Data.Type, content: (Binding<Data?>) -> V)`

Creates the immersive space for a specified type of presented data using view-
based content.

Available when `Content` conforms to `ImmersiveSpaceContent`, `Data` conforms
to `Decodable`, `Data` conforms to `Encodable`, and `Data` conforms to
`Hashable`.

`init(id: String, for: Data.Type, content: (Binding<Data?>) -> Content)`

Creates the immersive space associated with an identifier for a specified type
of presented data.

Initializer

# init(for:content:defaultValue:)

Creates an immersive space.

visionOS 1.0+

    
    
    init(
        for type: Data.Type = Data.self,
        @ImmersiveSpaceContentBuilder content: @escaping (Binding<Data>) -> Content,
        defaultValue: @escaping () -> Data
    )

##  Parameters

`type`

    

The type of presented data this immersive space accepts.

`content`

    

An immersive space content builder that defines the content for each instance
of the immersive space. The closure receives a binding to the value that you
pass to the `openImmersiveSpace` action when you call that action to open an
immersive space. The system automatically persists and restores the value of
this binding during state restoration.

`defaultValue`

    

A closure that returns a value that SwiftUI presents when it doesn’t receive
one from you, like when you call the `openImmersiveSpace` action without
providing a value.

## Discussion

The immersive space uses the specified content builder as a template to form
the content of the space. Your app invokes this initializer when it presents a
value of the specified `type` using the `openImmersiveSpace` action.

## See Also

### Providing default data to an immersive space

`init<V>(for: Data.Type, content: (Binding<Data>) -> V, defaultValue: () ->
Data)`

Creates an immersive space for a specified type of presented data and a
default value if the data is not set.

Available when `Content` conforms to `ImmersiveSpaceContent`, `Data` conforms
to `Decodable`, `Data` conforms to `Encodable`, and `Data` conforms to
`Hashable`.

`init<V>(id: String, for: Data.Type, content: (Binding<Data>) -> V,
defaultValue: () -> Data)`

Creates the immersive space associated with an identifier for a specified type
of presented data and a default value if the data is not set.

Available when `Content` conforms to `ImmersiveSpaceContent`, `Data` conforms
to `Decodable`, `Data` conforms to `Encodable`, and `Data` conforms to
`Hashable`.

`init(id: String, for: Data.Type, content: (Binding<Data>) -> Content,
defaultValue: () -> Data)`

Creates the immersive space associated with an identifier for a specified type
of presented data, and a default value, if the data is not set.

Initializer

# init(for:content:defaultValue:)

Creates an immersive space for a specified type of presented data and a
default value if the data is not set.

visionOS 1.0+

    
    
    init<V>(
        for type: Data.Type = Data.self,
        @ViewBuilder content: @escaping (Binding<Data>) -> V,
        defaultValue: @escaping () -> Data
    ) where Content == ImmersiveSpaceViewContent<V>, V : View

Available when `Content` conforms to `ImmersiveSpaceContent`, `Data` conforms
to `Decodable`, `Data` conforms to `Encodable`, and `Data` conforms to
`Hashable`.

##  Parameters

`type`

    

The type of presented data this immersive space accepts.

`content`

    

A view builder that defines the content for each instance of the immersive
space. The closure receives a binding to the value that you pass to the
`openImmersiveSpace` action when you use it to open an immersive space. The
system automatically persists and restores the value of this binding during
state restoration.

`defaultValue`

    

A closure that returns a value that SwiftUI presents when it doesn’t receive
one from you, like when you call the `openImmersiveSpace` action without
providing a value.

## Discussion

The immersive space uses the specified view as a template to form the content
of the space. Your app invokes this initializer when it presents a value of
the specified `type` using the `openImmersiveSpace` action.

## See Also

### Providing default data to an immersive space

`init(for: Data.Type, content: (Binding<Data>) -> Content, defaultValue: () ->
Data)`

Creates an immersive space.

`init<V>(id: String, for: Data.Type, content: (Binding<Data>) -> V,
defaultValue: () -> Data)`

Creates the immersive space associated with an identifier for a specified type
of presented data and a default value if the data is not set.

Available when `Content` conforms to `ImmersiveSpaceContent`, `Data` conforms
to `Decodable`, `Data` conforms to `Encodable`, and `Data` conforms to
`Hashable`.

`init(id: String, for: Data.Type, content: (Binding<Data>) -> Content,
defaultValue: () -> Data)`

Creates the immersive space associated with an identifier for a specified type
of presented data, and a default value, if the data is not set.

Initializer

# init(id:for:content:defaultValue:)

Creates the immersive space associated with an identifier for a specified type
of presented data and a default value if the data is not set.

visionOS 1.0+

    
    
    init<V>(
        id: String,
        for type: Data.Type = Data.self,
        @ViewBuilder content: @escaping (Binding<Data>) -> V,
        defaultValue: @escaping () -> Data
    ) where Content == ImmersiveSpaceViewContent<V>, V : View

Available when `Content` conforms to `ImmersiveSpaceContent`, `Data` conforms
to `Decodable`, `Data` conforms to `Encodable`, and `Data` conforms to
`Hashable`.

##  Parameters

`id`

    

A string that uniquely identifies the immersive space. Ensure that identifiers
are unique among the immersive spaces in your app.

`type`

    

The type of presented data this immersive space accepts.

`content`

    

A view builder that defines the content for each instance of the immersive
space. The closure receives a binding to the value that you pass to the
`openImmersiveSpace` action when you use it to open an immersive space. The
system automatically persists and restores the value of this binding during
state restoration.

`defaultValue`

    

A closure that returns a value that SwiftUI presents when it doesn’t receive
one from you, like when you call the `openImmersiveSpace` action without
providing a value.

## Discussion

The immersive space uses the specified view as a template to form the content
of the space. Your app invokes this initializer when it presents a value of
the specified `type` using the `openImmersiveSpace` action.

## See Also

### Providing default data to an immersive space

`init(for: Data.Type, content: (Binding<Data>) -> Content, defaultValue: () ->
Data)`

Creates an immersive space.

`init<V>(for: Data.Type, content: (Binding<Data>) -> V, defaultValue: () ->
Data)`

Creates an immersive space for a specified type of presented data and a
default value if the data is not set.

Available when `Content` conforms to `ImmersiveSpaceContent`, `Data` conforms
to `Decodable`, `Data` conforms to `Encodable`, and `Data` conforms to
`Hashable`.

`init(id: String, for: Data.Type, content: (Binding<Data>) -> Content,
defaultValue: () -> Data)`

Creates the immersive space associated with an identifier for a specified type
of presented data, and a default value, if the data is not set.

Initializer

# init(id:for:content:defaultValue:)

Creates the immersive space associated with an identifier for a specified type
of presented data, and a default value, if the data is not set.

visionOS 1.0+

    
    
    init(
        id: String,
        for type: Data.Type = Data.self,
        @ImmersiveSpaceContentBuilder content: @escaping (Binding<Data>) -> Content,
        defaultValue: @escaping () -> Data
    )

##  Parameters

`id`

    

A string that uniquely identifies the immersive space. Ensure that identifiers
are unique among the immersive spaces in your app.

`type`

    

The type of presented data this immersive space accepts.

`content`

    

An immersive space content builder that defines the content for each instance
of the immersive space. The closure receives a binding to the value that you
pass to the `openImmersiveSpace` action when you call that action to open an
immersive space. The system automatically persists and restores the value of
this binding during state restoration.

`defaultValue`

    

A closure that returns a value that SwiftUI presents when it doesn’t receive
one from you, like when you call the `openImmersiveSpace` action without
providing a value.

## Discussion

The space uses the specified content builder to form the content. Your app
invokes this initializer when it presents a value of the specified `type`
using the `openImmersiveSpace` action.

## See Also

### Providing default data to an immersive space

`init(for: Data.Type, content: (Binding<Data>) -> Content, defaultValue: () ->
Data)`

Creates an immersive space.

`init<V>(for: Data.Type, content: (Binding<Data>) -> V, defaultValue: () ->
Data)`

Creates an immersive space for a specified type of presented data and a
default value if the data is not set.

Available when `Content` conforms to `ImmersiveSpaceContent`, `Data` conforms
to `Decodable`, `Data` conforms to `Encodable`, and `Data` conforms to
`Hashable`.

`init<V>(id: String, for: Data.Type, content: (Binding<Data>) -> V,
defaultValue: () -> Data)`

Creates the immersive space associated with an identifier for a specified type
of presented data and a default value if the data is not set.

Available when `Content` conforms to `ImmersiveSpaceContent`, `Data` conforms
to `Decodable`, `Data` conforms to `Encodable`, and `Data` conforms to
`Hashable`.

Structure

# ImmersiveSpaceViewContent

Immersive space content that uses a SwiftUI view hierarchy as the content.

visionOS 1.0+

    
    
    struct ImmersiveSpaceViewContent<Content> where Content : View

## Overview

You don’t create this type directly. SwiftUI creates it when you construct an
`ImmersiveSpace` with view-based content.

## Relationships

### Conforms To

  * `ImmersiveSpaceContent`

## See Also

### Supporting types

`protocol ImmersiveSpaceContent`

A type that you can use as the content of an immersive space.

Protocol

# ImmersiveSpaceContent

A type that you can use as the content of an immersive space.

visionOS 1.0+

    
    
    protocol ImmersiveSpaceContent

## Topics

### Creating immersive space content

`var body: Self.Body`

**Required**

` associatedtype Body : ImmersiveSpaceContent`

**Required**

## Relationships

### Conforming Types

  * `ImmersiveSpaceViewContent`

## See Also

### Supporting types

`struct ImmersiveSpaceViewContent`

Immersive space content that uses a SwiftUI view hierarchy as the content.

Initializer

# init(content:)

Creates an immersive space.

visionOS 1.0+

    
    
    init(@ImmersiveSpaceContentBuilder content: @escaping () -> Content) where Data == Never

##  Parameters

`content`

    

An immersive space content builder that defines the content of the space.

## Discussion

The space uses the specified content builder to form the content.

Initializer

# init(content:)

Creates an immersive space using view-based content.

visionOS 1.0+

    
    
    init<V>(@ViewBuilder content: @escaping () -> V) where Content == ImmersiveSpaceViewContent<V>, Data == Never, V : View

Available when `Content` conforms to `ImmersiveSpaceContent`, `Data` conforms
to `Decodable`, `Data` conforms to `Encodable`, and `Data` conforms to
`Hashable`.

##  Parameters

`content`

    

A view builder that defines the content for each instance of the immersive
space.

## Discussion

The immersive space uses the specified view as a template to form the content
of the space.

Initializer

# init(id:content:)

Creates the immersive space associated with the specified identifier using
view-based content.

visionOS 1.0+

    
    
    init<V>(
        id: String,
        @ViewBuilder content: () -> V
    ) where Content == ImmersiveSpaceViewContent<V>, Data == Never, V : View

Available when `Content` conforms to `ImmersiveSpaceContent`, `Data` conforms
to `Decodable`, `Data` conforms to `Encodable`, and `Data` conforms to
`Hashable`.

##  Parameters

`id`

    

A string that uniquely identifies the immersive space. Ensure that identifiers
are unique among the immersive spaces in your app.

`content`

    

A view builder that defines the content for each instance of the immersive
space.

## Discussion

The immersive space uses the specified view as a template to form the content
of the space.

Initializer

# init(id:content:)

Creates the immersive space associated with the specified identifier.

visionOS 1.0+

    
    
    init(
        id: String,
        @ImmersiveSpaceContentBuilder content: () -> Content
    ) where Data == Never

##  Parameters

`id`

    

A string that uniquely identifies the immersive space. Ensure that identifiers
are unique among the immersive spaces in your app.

`content`

    

An immersive space content builder that defines the content of the space.

## Discussion

The space uses the specified content builder to form the content.

