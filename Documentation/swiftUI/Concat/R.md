# RadialGradient

Initializer

# init(gradient:center:startRadius:endRadius:)

Creates a radial gradient from a base gradient.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init(
        gradient: Gradient,
        center: UnitPoint,
        startRadius: CGFloat,
        endRadius: CGFloat
    )

## See Also

### Creating a radial gradient

`init(colors: [Color], center: UnitPoint, startRadius: CGFloat, endRadius:
CGFloat)`

Creates a radial gradient from a collection of colors.

`init(stops: [Gradient.Stop], center: UnitPoint, startRadius: CGFloat,
endRadius: CGFloat)`

Creates a radial gradient from a collection of color stops.

Initializer

# init(colors:center:startRadius:endRadius:)

Creates a radial gradient from a collection of colors.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init(
        colors: [Color],
        center: UnitPoint,
        startRadius: CGFloat,
        endRadius: CGFloat
    )

## See Also

### Creating a radial gradient

`init(gradient: Gradient, center: UnitPoint, startRadius: CGFloat, endRadius:
CGFloat)`

Creates a radial gradient from a base gradient.

`init(stops: [Gradient.Stop], center: UnitPoint, startRadius: CGFloat,
endRadius: CGFloat)`

Creates a radial gradient from a collection of color stops.

Initializer

# init(stops:center:startRadius:endRadius:)

Creates a radial gradient from a collection of color stops.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init(
        stops: [Gradient.Stop],
        center: UnitPoint,
        startRadius: CGFloat,
        endRadius: CGFloat
    )

## See Also

### Creating a radial gradient

`init(gradient: Gradient, center: UnitPoint, startRadius: CGFloat, endRadius:
CGFloat)`

Creates a radial gradient from a base gradient.

`init(colors: [Color], center: UnitPoint, startRadius: CGFloat, endRadius:
CGFloat)`

Creates a radial gradient from a collection of colors.



# RotatedShape

Initializer

# init(shape:angle:anchor:)

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init(
        shape: Content,
        angle: Angle,
        anchor: UnitPoint = .center
    )

Instance Property

# anchor

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var anchor: UnitPoint

## See Also

### Getting the shape’s characteristics

`var angle: Angle`

`var shape: Content`

Instance Property

# angle

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var angle: Angle

## See Also

### Getting the shape’s characteristics

`var anchor: UnitPoint`

`var shape: Content`

Instance Property

# shape

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var shape: Content

## See Also

### Getting the shape’s characteristics

`var anchor: UnitPoint`

`var angle: Angle`

Instance Property

# animatableData

The data to animate.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var animatableData: RotatedShape<Content>.AnimatableData { get set }



# ResetFocusAction

Instance Method

# callAsFunction(in:)

Asks the focus sytem to reevaluate the default focus item.

macOS 12.0+  tvOS 14.0+  watchOS 7.0+

    
    
    func callAsFunction(in namespace: Namespace.ID)

##  Parameters

`namespace`

    

The namespace inside which SwiftUI should reevaluate default focus. The
namespace should match the `focusScope(_:)` block where focus requires
reevaluation.

## Discussion

The focus system reevaluates default focus when the currently-focused item is
within the provided namespace.



# Rectangle

Initializer

# init()

Creates a new rectangle shape.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init()



# RenameButton

Initializer

# init()

Creates a rename button.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    init() where Label == Label<Text, Image>

Initializer

# init()

Creates a rename button.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    init() where Label == Label<Text, Image>



# RoundedRectangle

Initializer

# init(cornerRadius:style:)

Creates a new rounded rectangle shape.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init(
        cornerRadius: CGFloat,
        style: RoundedCornerStyle = .continuous
    )

##  Parameters

`cornerRadius`

    

the radius of the rounded corners.

`style`

    

the style of corners drawn by the shape.

## See Also

### Creating a rounded rectangle

`init(cornerSize: CGSize, style: RoundedCornerStyle)`

Creates a new rounded rectangle shape.

Initializer

# init(cornerSize:style:)

Creates a new rounded rectangle shape.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init(
        cornerSize: CGSize,
        style: RoundedCornerStyle = .continuous
    )

##  Parameters

`cornerSize`

    

the width and height of the rounded corners.

`style`

    

the style of corners drawn by the shape.

## See Also

### Creating a rounded rectangle

`init(cornerRadius: CGFloat, style: RoundedCornerStyle)`

Creates a new rounded rectangle shape.

Instance Property

# cornerSize

The width and height of the rounded rectangle’s corners.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var cornerSize: CGSize

## See Also

### Getting the shape’s characteristics

`var style: RoundedCornerStyle`

The style of corners drawn by the rounded rectangle.

Instance Property

# style

The style of corners drawn by the rounded rectangle.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var style: RoundedCornerStyle

## See Also

### Getting the shape’s characteristics

`var cornerSize: CGSize`

The width and height of the rounded rectangle’s corners.

Instance Property

# animatableData

The data to animate.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var animatableData: CGSize.AnimatableData { get set }



# RoundedCornerStyle

Case

# RoundedCornerStyle.circular

Quarter-circle rounded rect corners.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    case circular

## See Also

### Getting corner styles

`case continuous`

Continuous curvature rounded rect corners.

Case

# RoundedCornerStyle.continuous

Continuous curvature rounded rect corners.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    case continuous

## See Also

### Getting corner styles

`case circular`

Quarter-circle rounded rect corners.



# RotateGesture

Initializer

# init(minimumAngleDelta:)

Creates a rotation gesture with a minimum delta for the gesture to start.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    init(minimumAngleDelta: Angle = .degrees(1))

##  Parameters

`minimumAngleDelta`

    

The minimum delta required before the gesture starts. The default value is a
one-degree angle.

## See Also

### Creating the gesture

`var minimumAngleDelta: Angle`

The minimum delta required before the gesture succeeds.

Instance Property

# minimumAngleDelta

The minimum delta required before the gesture succeeds.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    var minimumAngleDelta: Angle

## See Also

### Creating the gesture

`init(minimumAngleDelta: Angle)`

Creates a rotation gesture with a minimum delta for the gesture to start.



# RoundedBorderTextEditorStyle

Initializer

# init()

visionOS 1.0+

    
    
    init()



# RoundedBorderTextFieldStyle

Initializer

# init()

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  visionOS 1.0+

    
    
    init()



# RadioGroupPickerStyle

Initializer

# init()

Creates a radio group picker style.

macOS 10.15+

    
    
    init()



# RotateGesture3D

Initializer

# init(constrainedToAxis:minimumAngleDelta:)

Creates a rotation gesture with a minimum delta for the gesture to start and
axis to constrain measurement of rotation.

visionOS 1.0+

    
    
    init(
        constrainedToAxis: RotationAxis3D? = nil,
        minimumAngleDelta: Angle = .degrees(1)
    )

##  Parameters

`constrainedToAxis`

    

The 3D axis about which rotation is measured.

`minimumAngleDelta`

    

The minimum delta required before the gesture starts. The default value is a
one-degree angle.

## Discussion

If the constrained axis is `nil`, the gesture measures unconstrained 3D
rotation.

## See Also

### Creating the gesture

`var minimumAngleDelta: Angle`

The minimum angle delta before the gesture becomes active.

`var constrainedAxis: RotationAxis3D?`

An axis around which the rotation is constrained.

Instance Property

# minimumAngleDelta

The minimum angle delta before the gesture becomes active.

visionOS 1.0+

    
    
    var minimumAngleDelta: Angle

## See Also

### Creating the gesture

`init(constrainedToAxis: RotationAxis3D?, minimumAngleDelta: Angle)`

Creates a rotation gesture with a minimum delta for the gesture to start and
axis to constrain measurement of rotation.

`var constrainedAxis: RotationAxis3D?`

An axis around which the rotation is constrained.

Instance Property

# constrainedAxis

An axis around which the rotation is constrained.

visionOS 1.0+

    
    
    var constrainedAxis: RotationAxis3D?

## Discussion

If the axis is `nil`, the rotation is unconstrained.

## See Also

### Creating the gesture

`init(constrainedToAxis: RotationAxis3D?, minimumAngleDelta: Angle)`

Creates a rotation gesture with a minimum delta for the gesture to start and
axis to constrain measurement of rotation.

`var minimumAngleDelta: Angle`

The minimum angle delta before the gesture becomes active.



# ReferenceFileDocumentConfiguration

Instance Property

# document

The current document model.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    @ObservedObject @MainActor
    var document: Document { get set }

## Discussion

Changes to the document dirty the document state, indicating that it needs to
be saved. SwiftUI doesn’t automatically register undo actions. You have to
manage undo operations yourself, as demonstrated in Building a Document-Based
App with SwiftUI.

## See Also

### Getting and setting the document

`var $document: ObservedObject<Document>.Wrapper`

Instance Property

# $document

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    @MainActor
    var $document: ObservedObject<Document>.Wrapper { get }

## See Also

### Getting and setting the document

`var document: Document`

The current document model.

Instance Property

# fileURL

The URL of the open file document.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    @MainActor
    var fileURL: URL?

## See Also

### Getting document properties

`var isEditable: Bool`

A Boolean that indicates whether you can edit the document.

Instance Property

# isEditable

A Boolean that indicates whether you can edit the document.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    @MainActor
    var isEditable: Bool

## Discussion

The value is `false` if the document is in viewing mode, or if the file is not
writable.

## See Also

### Getting document properties

`var fileURL: URL?`

The URL of the open file document.



# RenameAction

Instance Method

# callAsFunction()

Triggers the standard rename action provided through the environment.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func callAsFunction()



# RefreshAction

Instance Method

# callAsFunction()

Initiates a refresh action.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func callAsFunction() async

## Discussion

Don’t call this method directly. SwiftUI calls it when you call the
`RefreshAction` structure that you get from the `Environment`:

For information about how Swift uses the `callAsFunction()` method to simplify
call site syntax, see Methods with Special Names in _The Swift Programming
Language_. For information about asynchronous operations in Swift, see
Concurrency.



# RectangleCornerRadii

Initializer

# init(topLeading:bottomLeading:bottomTrailing:topTrailing:)

Creates a new set of corner radii for a rounded rectangle with uneven corners.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    init(
        topLeading: CGFloat = 0,
        bottomLeading: CGFloat = 0,
        bottomTrailing: CGFloat = 0,
        topTrailing: CGFloat = 0
    )

##  Parameters

`topLeading`

    

the radius of the top-leading corner.

`bottomLeading`

    

the radius of the bottom-leading corner.

`bottomTrailing`

    

the radius of the bottom-trailing corner.

`topTrailing`

    

the radius of the top-trailing corner.

Instance Property

# topLeading

The radius of the top-leading corner.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    var topLeading: CGFloat { get set }

## See Also

### Getting values for specific corners

`var topTrailing: CGFloat`

The radius of the top-trailing corner.

`var bottomLeading: CGFloat`

The radius of the bottom-leading corner.

`var bottomTrailing: CGFloat`

The radius of the bottom-trailing corner.

Instance Property

# topTrailing

The radius of the top-trailing corner.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    var topTrailing: CGFloat { get set }

## See Also

### Getting values for specific corners

`var topLeading: CGFloat`

The radius of the top-leading corner.

`var bottomLeading: CGFloat`

The radius of the bottom-leading corner.

`var bottomTrailing: CGFloat`

The radius of the bottom-trailing corner.

Instance Property

# bottomLeading

The radius of the bottom-leading corner.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    var bottomLeading: CGFloat { get set }

## See Also

### Getting values for specific corners

`var topLeading: CGFloat`

The radius of the top-leading corner.

`var topTrailing: CGFloat`

The radius of the top-trailing corner.

`var bottomTrailing: CGFloat`

The radius of the bottom-trailing corner.

Instance Property

# bottomTrailing

The radius of the bottom-trailing corner.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    var bottomTrailing: CGFloat { get set }

## See Also

### Getting values for specific corners

`var topLeading: CGFloat`

The radius of the top-leading corner.

`var topTrailing: CGFloat`

The radius of the top-trailing corner.

`var bottomLeading: CGFloat`

The radius of the bottom-leading corner.



# ReferenceFileDocument

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

# ReferenceFileDocument.ReadConfiguration

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

# snapshot(contentType:)

Creates a snapshot that represents the current state of the document.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    func snapshot(contentType: UTType) throws -> Self.Snapshot

**Required**

##  Parameters

`contentType`

    

The content type that you create the document snapshot for.

## Return Value

A snapshot of the document content that the system provides to the
`fileWrapper(snapshot:configuration:)` method for serialization.

## Discussion

To store a document — for example, in response to a Save command — SwiftUI
begins by calling this method. Return a copy of the document’s content from
your implementation of the method. For example, you might define an
initializer for your document’s model object that copies the contents of the
document’s instance, and return that:

SwiftUI prevents document edits during the snapshot operation to ensure that
the model state remains coherent. After the call completes, SwiftUI reenables
edits, and then calls the `fileWrapper(snapshot:configuration:)` method, where
you serialize the snapshot and store it to a file.

Note

SwiftUI calls this method on a background thread. Don’t make user interface
changes from that thread.

## See Also

### Getting a snapshot

`associatedtype Snapshot`

A type that represents the document’s stored content.

**Required**

Associated Type

# Snapshot

A type that represents the document’s stored content.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    associatedtype Snapshot

**Required**

## Discussion

Define this type to represent all the data that your document stores. When
someone issues a Save command, SwiftUI asks your document for a value of this
type by calling the document’s `snapshot(contentType:)` method. SwiftUI sends
the snapshot that you provide to the document’s
`fileWrapper(snapshot:configuration:)` method, where you serialize the
contents of the snapshot into a file wrapper.

## See Also

### Getting a snapshot

`func snapshot(contentType: UTType) throws -> Self.Snapshot`

Creates a snapshot that represents the current state of the document.

**Required**

Instance Method

# fileWrapper(snapshot:configuration:)

Serializes a document snapshot to a file wrapper.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    func fileWrapper(
        snapshot: Self.Snapshot,
        configuration: Self.WriteConfiguration
    ) throws -> FileWrapper

**Required**

##  Parameters

`snapshot`

    

The document snapshot to save.

`configuration`

    

Information about a file that already exists for the document, if any.

## Return Value

The destination to serialize the document contents to. The value can be a
newly created `FileWrapper` or an update of the one provided in the
`configuration` input.

## Discussion

To store a document — for example, in response to a Save command — SwiftUI
begins by calling the `snapshot(contentType:)` method to get a copy of the
document data in its current state. Then SwiftUI passes that snapshot to this
method, where you serialize it and create or modify a file wrapper with the
serialized data:

SwiftUI disables document edits during the snapshot to ensure that the
document’s data remains coherent, but reenables edits during the serialization
operation.

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

### ReferenceFileDocument Implementations

`static var writableContentTypes: [UTType]`

The file types that the document supports saving or exporting to.

## See Also

### Writing a document

`func fileWrapper(snapshot: Self.Snapshot, configuration:
Self.WriteConfiguration) throws -> FileWrapper`

Serializes a document snapshot to a file wrapper.

**Required**

` typealias WriteConfiguration`

The configuration for writing document contents.

Type Alias

# ReferenceFileDocument.WriteConfiguration

The configuration for writing document contents.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    typealias WriteConfiguration = FileDocumentWriteConfiguration

## Discussion

This type is an alias for `FileDocumentWriteConfiguration`, which contains a
content type and a file wrapper that you use to access the contents of a
document file, if one already exists. You get a value of this type as an input
to the `fileWrapper(snapshot:configuration:)` method.

## See Also

### Writing a document

`func fileWrapper(snapshot: Self.Snapshot, configuration:
Self.WriteConfiguration) throws -> FileWrapper`

Serializes a document snapshot to a file wrapper.

**Required**

` static var writableContentTypes: [UTType]`

The file types that the document supports saving or exporting to.

**Required** Default implementation provided.



# RedactionReasons

Type Property

# invalidated

Displayed data should appear as invalidated and pending a new update.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    static let invalidated: RedactionReasons

## Discussion

Views marked with `invalidatableContent` will be automatically redacted with a
standard styling indicating the content is invalidated and new content will be
available soon.

## See Also

### Getting redaction reasons

`static let placeholder: RedactionReasons`

Displayed data should appear as generic placeholders.

`static let privacy: RedactionReasons`

Displayed data should be obscured to protect private information.

Type Property

# placeholder

Displayed data should appear as generic placeholders.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    static let placeholder: RedactionReasons

## Discussion

Text and images will be automatically masked to appear as generic
placeholders, though maintaining their original size and shape. Use this to
create a placeholder UI without directly exposing placeholder data to users.

## See Also

### Getting redaction reasons

`static let invalidated: RedactionReasons`

Displayed data should appear as invalidated and pending a new update.

`static let privacy: RedactionReasons`

Displayed data should be obscured to protect private information.

Type Property

# privacy

Displayed data should be obscured to protect private information.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static let privacy: RedactionReasons

## Discussion

Views marked with `privacySensitive` will be automatically redacted using a
standard styling. To apply a custom treatment the redaction reason can be read
out of the environment.

## See Also

### Getting redaction reasons

`static let invalidated: RedactionReasons`

Displayed data should appear as invalidated and pending a new update.

`static let placeholder: RedactionReasons`

Displayed data should appear as generic placeholders.

Initializer

# init(rawValue:)

Creates a new set from a raw value.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    init(rawValue: Int)

##  Parameters

`rawValue`

    

The raw value with which to create the reasons for redaction.

## See Also

### Creating redaction reasons

`let rawValue: Int`

The raw value.

Instance Property

# rawValue

The raw value.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    let rawValue: Int

## See Also

### Creating redaction reasons

`init(rawValue: Int)`

Creates a new set from a raw value.



# RotationGesture

Initializer

# init(minimumAngleDelta:)

Creates a rotation gesture with a minimum delta for the gesture to start.

iOS 13.0–17.4  Deprecated  iPadOS 13.0–17.4  Deprecated  macOS 10.15–14.4
Deprecated  Mac Catalyst 13.0–17.4  Deprecated  visionOS 1.0+

    
    
    init(minimumAngleDelta: Angle = .degrees(1))

Deprecated

Use `RotateGesture` instead.

## See Also

### Creating the gesture

`var minimumAngleDelta: Angle`

The minimum delta required before the gesture succeeds.

Deprecated

Instance Property

# minimumAngleDelta

The minimum delta required before the gesture succeeds.

iOS 13.0–17.4  Deprecated  iPadOS 13.0–17.4  Deprecated  macOS 10.15–14.4
Deprecated  Mac Catalyst 13.0–17.4  Deprecated  visionOS 1.0+

    
    
    var minimumAngleDelta: Angle

Deprecated

Use `RotateGesture` instead.

## See Also

### Creating the gesture

`init(minimumAngleDelta: Angle)`

Creates a rotation gesture with a minimum delta for the gesture to start.

Deprecated



