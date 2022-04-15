using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using DG.Tweening;
using System;
using UnityEngine.UI;

public class SwitchHandler : MonoBehaviour{
  public bool switchState;
  private bool switchState2;
  public GameObject switchBtn;
  private float curX;
  public Image img;
  private Color32[] cols;
  

  public void Start(){
    curX=Mathf.Abs(switchBtn.transform.localPosition.x);
    switchState2=switchState=(switchBtn.transform.localPosition.x<0)?false:true;;
    cols= new Color32[3];
    cols[0]=new Color32(255,0,0,255);
    cols[1]=new Color32(0,255,0,255);
    cols[2]=new Color32(100,100,100,255);
  }
  public void Update(){
    if (switchState!=switchState2){
      Tween x= switchBtn.transform.DOLocalMoveX(((switchState2?-1:1)*curX),0.2f);
      x.OnUpdate(()=>{
        img.color=cols[2];
      });
      x.OnComplete(()=>{ 
        img.color=((switchState)?cols[1]:cols[0]);
        });
      switchState2=switchState;
    }
  }

  public void OnSwitchButtonClicked(){
    switchState = !switchState2;
  }
  
}