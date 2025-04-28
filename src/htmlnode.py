class HTMLNode():
    def __init__(self,tag=None,value=None,children=None,props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise Exception(NotImplementedError)

    def props_to_html(self):
        if self.props is None:
            return ""
        result = ""
        for key,value in self.props.items():
            result += f' {key}="{value}"'
        return result

    def __eq__(self, other):
        return self.tag == other.tag and self.value == other.value and self.children == other.children and self.props == other.props

    def __repr__(self):
        return f"HTMLNode (tag:{self.tag}, value:{self.value}, children:{self.children}, props:{self.props})"

class ParentNode(HTMLNode):
    def __init__(self,tag, children, props=None):
        super().__init__(tag,None,children,props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("No tag")
        if self.children is []:
            raise ValueError("No children")
        return f"<{self.tag}{self.props_to_html()}>{''.join([child.to_html() for child in self.children])}</{self.tag}>"


class LeafNode(HTMLNode):
    def __init__(self,tag=None,value=None, props=None):
        super().__init__(tag,value,None,props)

    def to_html(self):
        if self.value is None:
            raise ValueError
        if self.tag is None:
            return self.value
        if self.props is None or self.props == {}:
            return f"<{self.tag}>{self.value}</{self.tag}>"
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
