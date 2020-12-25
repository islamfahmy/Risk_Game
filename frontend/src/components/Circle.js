
const Circle = props => {
    const { x, y, count, color ,r,id,Click} = props;
    const styler ={
    	position: "relative",
    	backgroundColor:color,
    	left:x,
    	top:y,
    	borderRadius:r,
    	fontSize: r, 
    }
    return <div>
    	<button style={styler} onClick= {()=>Click(id)}>
    		{count}
    	</button>
    </div>
}

export default Circle;
