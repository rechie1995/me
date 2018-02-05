// mysort.h
// Created by rechie on 2018/02/03.
//

#ifndef _MYSORT_H
#define _MYSORT_H

#ifdef __cplusplus
extern "C"{
#endif

// 插入排序
void InsertSort(int R[], int num);
// 选择排序
void SelectSort(int R[], int num);
// 冒泡排序
void BubbleSort(int R[], int num);
// 快速排序
void QuickSort(int R[], int l, int r);
// 堆排序
void Sift(int R[], int low, int high);
void HeapSort(int R[], int num);
#ifdef __cplusplus
}
#endif

#endif //_MYSORT_H