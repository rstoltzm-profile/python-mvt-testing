import pandas as pd
import numpy as np

# dataset
data = {
    'headline': ['Headline 1', 'Headline 2', 'Headline 3'],
    'image': ['Image A', 'Image B', 'Image C']
}


# create an empty list
combinations = []


def create_combinations(data):
    lengths = [len(v) for v in data.values()]
    print(lengths)
    for headline in data['headline']:
        for image in data['image']:
            combinations.append({'headline': headline, 'image': image})
    df = pd.DataFrame(combinations)
    return df


def randomize_usage(df):
    np.random.seed(42)
    df['clicks'] = np.random.randint(50, 150, size=len(df))
    df['views'] = np.random.randint(200, 300, size=len(df))
    df['ctr'] = df['clicks'] / df['views']
    df = df.sort_values(by='ctr', ascending=False) 
    print(df)
    return df


def return_results(df):
    best_combination = df.loc[df['ctr'].idxmax()]
    print("Best Combination:")
    print(f"Headline: {best_combination['headline']}, Image: {best_combination['image']}, CTR: {best_combination['ctr']:.2f}")


def main():
    df = create_combinations(data)
    df = randomize_usage(df)
    return_results(df)


if __name__ == "__main__":
    main()
