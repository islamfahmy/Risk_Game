const Circle = props => {
    const { x, y, count, color ,r} = props;
    const styler ={
    	position: "relative",
    	backgroundColor:color,
    	left:x,
    	top:y,
    	borderRadius:r,
    	fontSize: r, 
    }
    return <div>
    	<button style={styler}>
    		{count}
    	</button>
    </div>
}

export default Circle;
