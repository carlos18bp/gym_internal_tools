import{e as t,f as s,F as a,g as n,n as o,A as d,t as i}from"./index.js";const p="data:image/svg+xml,%3csvg%20width='24'%20height='25'%20viewBox='0%200%2024%2025'%20fill='none'%20xmlns='http://www.w3.org/2000/svg'%3e%3cpath%20d='M3.5%2010.5C3.5%206.72876%203.5%204.84315%204.7448%203.67157C5.98959%202.5%207.99306%202.5%2012%202.5H12.7727C16.0339%202.5%2017.6645%202.5%2018.7969%203.29784C19.1214%203.52643%2019.4094%203.79752%2019.6523%204.10289C20.5%205.16867%2020.5%206.70336%2020.5%209.77273V12.3182C20.5%2015.2814%2020.5%2016.7629%2020.0311%2017.9462C19.2772%2019.8486%2017.6829%2021.3491%2015.6616%2022.0586C14.4044%2022.5%2012.8302%2022.5%209.68182%2022.5C7.88275%2022.5%206.98322%2022.5%206.26478%2022.2478C5.10979%2021.8424%204.19875%2020.9849%203.76796%2019.8979C3.5%2019.2217%203.5%2018.3751%203.5%2016.6818V10.5Z'%20stroke='%233348FF'%20stroke-width='1.5'%20stroke-linejoin='round'/%3e%3cpath%20d='M20.5%2012.5C20.5%2014.3409%2019.0076%2015.8333%2017.1667%2015.8333C16.5009%2015.8333%2015.716%2015.7167%2015.0686%2015.8901C14.4935%2016.0442%2014.0442%2016.4935%2013.8901%2017.0686C13.7167%2017.716%2013.8333%2018.5009%2013.8333%2019.1667C13.8333%2021.0076%2012.3409%2022.5%2010.5%2022.5'%20stroke='%233348FF'%20stroke-width='1.5'%20stroke-linecap='round'%20stroke-linejoin='round'/%3e%3cpath%20d='M8%207.5H15'%20stroke='%233348FF'%20stroke-width='1.5'%20stroke-linecap='round'%20stroke-linejoin='round'/%3e%3cpath%20d='M8%2011.5H11'%20stroke='%233348FF'%20stroke-width='1.5'%20stroke-linecap='round'%20stroke-linejoin='round'/%3e%3c/svg%3e",g={class:"absolute top-1/2 left-0 right-0 z-10 transform -translate-y-1/2 flex w-full h-full px-16 justify-between items-center"},h=n("div",{class:"size-8 bg-secondary rounded-full"},null,-1),y=n("div",{class:"size-8 bg-secondary rounded-full"},null,-1),m=n("div",{class:"size-8 bg-secondary rounded-full"},null,-1),k={key:2,class:"size-16 bg-white border-2 border-secondary rounded-full"},C={__name:"Bubbles",props:{length:{type:Number,required:!0},displayParam:{type:String,required:!0}},setup(e){return(c,u)=>(t(),s("div",g,[e.length>2?(t(),s(a,{key:0},[h,y,n("div",{class:o(["size-16 rounded-full",e.displayParam==="history"?"bg-secondary":"bg-white border-2 border-secondary"])},null,2)],64)):e.length>1?(t(),s(a,{key:1},[m,n("div",{class:o(["size-16 rounded-full",e.displayParam==="history"?"bg-secondary":"bg-white border-2 border-secondary"])},null,2)],64)):(t(),s("div",k))]))}},b={class:"relative mt-5 px-16 flex justify-between items-center text-gray-500 font-medium"},w={key:2,class:"text-sm w-16 text-center"},x={__name:"TextStages",props:{stages:{type:Array,required:!0}},setup(e){return(c,u)=>(t(),s("div",b,[e.stages.length>2?(t(!0),s(a,{key:0},d(e.stages.slice(-3),(l,r)=>(t(),s("p",{key:r,class:o(["text-sm text-center",r===2?"w-16":"w-8"])},i(l.status),3))),128)):e.stages.length>1?(t(!0),s(a,{key:1},d(e.stages.slice(-2),(l,r)=>(t(),s("p",{key:r,class:o(["text-sm text-center",r===1?"w-16":"w-8"])},i(l.status),3))),128)):(t(),s("p",w,i(e.stages[0].status),1))]))}};export{C as _,x as a,p as b};
