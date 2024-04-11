Structure

# Anchor.Source

A type-erased geometry value that produces an anchored value of a given type.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @frozen
    struct Source

## Overview

SwiftUI passes anchored geometry values around the view tree via preference
keys. It then converts them back into the local coordinate space using a
`GeometryProxy` value.

## Topics

### Getting point anchor sources

`static func point(CGPoint) -> Anchor<Value>.Source`

Available when `Value` is `CGPoint`.

`static func unitPoint(UnitPoint) -> Anchor<Value>.Source`

Available when `Value` is `CGPoint`.

### Getting rectangle anchor sources

`static func rect(CGRect) -> Anchor<Value>.Source`

Returns an anchor source rect defined by `r` in the current view.

Available when `Value` is `CGRect`.

`static var bounds: Anchor<CGRect>.Source`

An anchor source rect defined as the entire bounding rect of the current view.

Available when `Value` is `CGRect`.

### Getting top anchor sources

`static var topLeading: Anchor<CGPoint>.Source`

Available when `Value` is `CGPoint`.

`static var top: Anchor<CGPoint>.Source`

Available when `Value` is `CGPoint`.

`static var topTrailing: Anchor<CGPoint>.Source`

Available when `Value` is `CGPoint`.

### Getting middle anchor sources

`static var leading: Anchor<CGPoint>.Source`

Available when `Value` is `CGPoint`.

`static var center: Anchor<CGPoint>.Source`

Available when `Value` is `CGPoint`.

`static var trailing: Anchor<CGPoint>.Source`

Available when `Value` is `CGPoint`.

### Getting bottom anchor sources

`static var bottomTrailing: Anchor<CGPoint>.Source`

Available when `Value` is `CGPoint`.

`static var bottom: Anchor<CGPoint>.Source`

Available when `Value` is `CGPoint`.

`static var bottomLeading: Anchor<CGPoint>.Source`

Available when `Value` is `CGPoint`.

### Creating an anchor source

`init<T>(Anchor<T>.Source?)`

`init<T>([Anchor<T>.Source])`

## Relationships

### Conforms To

  * `Sendable`

