Instance Property

# layoutDirection

The layout direction inherited by the container view.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    var layoutDirection: LayoutDirection

## Discussion

SwiftUI supports both left-to-right and right-to-left directions. Read this
property within a custom layout container to find out which environment the
container is in.

In most cases, you don’t need to take any action based on this value. SwiftUI
horizontally flips the x position of each view within its parent when the mode
switches, so layout calculations automatically produce the desired effect for
both directions.

Instance Subscript

# subscript(_:)

Gets the subview proxy at a specified index.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    subscript(index: Int) -> LayoutSubviews.Element { get }

## See Also

### Accessing subviews

`subscript<S>(S) -> LayoutSubviews`

Gets the subview proxies with the specified indicies.

`subscript(Range<Int>) -> LayoutSubviews`

Gets the subview proxies in the specified range.

`var startIndex: Int`

The index of the first subview.

`var endIndex: Int`

An index that’s one higher than the last subview.

`typealias Element`

A type that contains a proxy value.

`typealias Index`

A type that you can use to index proxy values.

`typealias SubSequence`

A type that contains a subsequence of proxy values.

Instance Subscript

# subscript(_:)

Gets the subview proxies with the specified indicies.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    subscript<S>(indices: S) -> LayoutSubviews where S : Sequence, S.Element == Int { get }

## See Also

### Accessing subviews

`subscript(Int) -> LayoutSubviews.Element`

Gets the subview proxy at a specified index.

`subscript(Range<Int>) -> LayoutSubviews`

Gets the subview proxies in the specified range.

`var startIndex: Int`

The index of the first subview.

`var endIndex: Int`

An index that’s one higher than the last subview.

`typealias Element`

A type that contains a proxy value.

`typealias Index`

A type that you can use to index proxy values.

`typealias SubSequence`

A type that contains a subsequence of proxy values.

Instance Subscript

# subscript(_:)

Gets the subview proxies in the specified range.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    subscript(bounds: Range<Int>) -> LayoutSubviews { get }

## See Also

### Accessing subviews

`subscript(Int) -> LayoutSubviews.Element`

Gets the subview proxy at a specified index.

`subscript<S>(S) -> LayoutSubviews`

Gets the subview proxies with the specified indicies.

`var startIndex: Int`

The index of the first subview.

`var endIndex: Int`

An index that’s one higher than the last subview.

`typealias Element`

A type that contains a proxy value.

`typealias Index`

A type that you can use to index proxy values.

`typealias SubSequence`

A type that contains a subsequence of proxy values.

Instance Property

# startIndex

The index of the first subview.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    var startIndex: Int { get }

## See Also

### Accessing subviews

`subscript(Int) -> LayoutSubviews.Element`

Gets the subview proxy at a specified index.

`subscript<S>(S) -> LayoutSubviews`

Gets the subview proxies with the specified indicies.

`subscript(Range<Int>) -> LayoutSubviews`

Gets the subview proxies in the specified range.

`var endIndex: Int`

An index that’s one higher than the last subview.

`typealias Element`

A type that contains a proxy value.

`typealias Index`

A type that you can use to index proxy values.

`typealias SubSequence`

A type that contains a subsequence of proxy values.

Instance Property

# endIndex

An index that’s one higher than the last subview.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    var endIndex: Int { get }

## See Also

### Accessing subviews

`subscript(Int) -> LayoutSubviews.Element`

Gets the subview proxy at a specified index.

`subscript<S>(S) -> LayoutSubviews`

Gets the subview proxies with the specified indicies.

`subscript(Range<Int>) -> LayoutSubviews`

Gets the subview proxies in the specified range.

`var startIndex: Int`

The index of the first subview.

`typealias Element`

A type that contains a proxy value.

`typealias Index`

A type that you can use to index proxy values.

`typealias SubSequence`

A type that contains a subsequence of proxy values.

Type Alias

# LayoutSubviews.Element

A type that contains a proxy value.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    typealias Element = LayoutSubview

## See Also

### Accessing subviews

`subscript(Int) -> LayoutSubviews.Element`

Gets the subview proxy at a specified index.

`subscript<S>(S) -> LayoutSubviews`

Gets the subview proxies with the specified indicies.

`subscript(Range<Int>) -> LayoutSubviews`

Gets the subview proxies in the specified range.

`var startIndex: Int`

The index of the first subview.

`var endIndex: Int`

An index that’s one higher than the last subview.

`typealias Index`

A type that you can use to index proxy values.

`typealias SubSequence`

A type that contains a subsequence of proxy values.

Type Alias

# LayoutSubviews.Index

A type that you can use to index proxy values.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    typealias Index = Int

## See Also

### Accessing subviews

`subscript(Int) -> LayoutSubviews.Element`

Gets the subview proxy at a specified index.

`subscript<S>(S) -> LayoutSubviews`

Gets the subview proxies with the specified indicies.

`subscript(Range<Int>) -> LayoutSubviews`

Gets the subview proxies in the specified range.

`var startIndex: Int`

The index of the first subview.

`var endIndex: Int`

An index that’s one higher than the last subview.

`typealias Element`

A type that contains a proxy value.

`typealias SubSequence`

A type that contains a subsequence of proxy values.

Type Alias

# LayoutSubviews.SubSequence

A type that contains a subsequence of proxy values.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    typealias SubSequence = LayoutSubviews

## See Also

### Accessing subviews

`subscript(Int) -> LayoutSubviews.Element`

Gets the subview proxy at a specified index.

`subscript<S>(S) -> LayoutSubviews`

Gets the subview proxies with the specified indicies.

`subscript(Range<Int>) -> LayoutSubviews`

Gets the subview proxies in the specified range.

`var startIndex: Int`

The index of the first subview.

`var endIndex: Int`

An index that’s one higher than the last subview.

`typealias Element`

A type that contains a proxy value.

`typealias Index`

A type that you can use to index proxy values.

